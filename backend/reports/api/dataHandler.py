import requests
import datetime
import sqlite3


def update_database():
    urls = {
        'statistics_get_report': 'https://statistics-api.wildberries.ru/api/v5/supplier/reportDetailByPeriod'}

    url = urls['statistics_get_report']
    db_path = "/Users/dianahazgalieva/Desktop/analytic_service/backend/db.sqlite3"
    api_key = "eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQwMjI2djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTcyODk0NTU5MSwiaWQiOiI3YThjNWM2OS02ZmQyLTQyMDYtOTJmYy0wZDk3Zjc2ZTNmMTEiLCJpaWQiOjU5MTY0MDE5LCJvaWQiOjExNjI3NzcsInMiOjQ0LCJzaWQiOiI5YzVhYjQ5MS1jNjkzLTQ1M2QtYjIxMC1jZmM3MzgyOWIwMjEiLCJ0IjpmYWxzZSwidWlkIjo1OTE2NDAxOX0.-_B3tBks_1q1OaTLs6JKewzsX5KcumxQygYDEJoWNRlUiv8TLKXwlBGgXR86kB9gsv9koh8Y0OYsnWE8v3T0OA"

    headers = {
        "Authorization": api_key
    }

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # today = datetime.datetime.now().replace(microsecond=0).isoformat()
    # last_week = (datetime.datetime.now().replace(microsecond=0) - datetime.timedelta(days=7)).isoformat()

    today = '2024-04-28T00:00:00'
    last_week = '2024-04-22T00:00:00'

    cursor.execute('SELECT * FROM reports_information')
    exact_date = cursor.fetchone()
    if exact_date != None and exact_date[1] == last_week and exact_date[2] == today:
        return

    tables = ['`reports_storage`', '`reports_sales`', '`reports_returns`',
              '`reports_logistics`', '`reports_other`', '`reports_information`']
    for t in tables:
        cursor.execute('DELETE FROM %s' % t)
    connection.commit()

    get_params = {
        "dateFrom": last_week,
        "dateTo": today
    }

    response = requests.get(url, headers=headers, params=get_params)
    if (response.status_code != 200):
        print(response.text)
        return
    cursor.execute(
        'INSERT OR REPLACE INTO reports_information (date_from, date_to) VALUES (?, ?)', (last_week, today))
    result = response.json()

    storage_fee = 0
    recount_storaging = 0
    delivery_amount = 0
    delivery_amount_price = 0
    return_amount = 0
    return_amount_price = 0
    fines = 0
    surchages = 0
    compensation = 0

    for i in result:
        supplier_oper_name = i['supplier_oper_name']
        if supplier_oper_name == 'Хранение':
            storage_fee += i['storage_fee']
        elif supplier_oper_name == 'Пересчет хранения':
            recount_storaging -= i['storage_fee']
        elif supplier_oper_name == 'Компенсация брака':
            compensation += i['ppvz_for_pay']
        elif supplier_oper_name == 'Продажа':
            real_price = i['retail_amount']
            comission = i['ppvz_reward'] + i['acquiring_fee'] + \
                i['ppvz_vw'] + i['ppvz_vw_nds']
            income = i['ppvz_for_pay']
            product_name = ""
            nm_id = i['nm_id']
            cursor.execute(
                'SELECT name FROM products_product WHERE nmID = ?', (nm_id, ))
            product_name = cursor.fetchone()[0]
            cursor.execute(
                'INSERT OR REPLACE INTO reports_sales (real_price, comission, income, product_name, nm_id) VALUES (?,?,?,?,?)',
                (real_price, comission, income, product_name, nm_id))
        elif supplier_oper_name == 'Возврат':
            nm_id = i['nm_id']
            cursor.execute(
                'SELECT name FROM products_product WHERE nmID = ?', (nm_id, ))
            product_name = cursor.fetchone()[0]
            refund_amount = i['retail_amount']
            cursor.execute(
                'INSERT OR REPLACE INTO reports_returns (refund_amount, product_name, nm_id) VALUES (?,?,?)',
                (refund_amount, product_name, nm_id))
        elif supplier_oper_name == 'Логистика':
            if i['delivery_amount'] == 1:
                delivery_amount += 1
                delivery_amount_price += i['delivery_rub']
            elif i['return_amount'] == 1:
                return_amount += 1
                return_amount_price += i['delivery_rub']
        elif supplier_oper_name == 'Штрафы':
            fines += i['penalty']
        elif supplier_oper_name == 'Доплаты':
            surchages += i['additional_payment']
        elif supplier_oper_name == 'Возмещение издержек по перевозке/по складским операциям с товаром':
            surchages -= i['ppvz_vw'] - i['ppvz_vw_nds']

    cursor.execute(
        'INSERT OR REPLACE INTO reports_storage (storaging, recount_storaging, acceptanse) VALUES (?,?,?)',
        (round(storage_fee, 2), round(recount_storaging, 2), 0))
    average_price = round((delivery_amount_price / delivery_amount), 2)
    average_price_r = round((return_amount_price / return_amount), 2)
    cursor.execute(
        'INSERT OR REPLACE INTO reports_logistics (number, amount, average_price) VALUES (?,?,?)',
        (delivery_amount, delivery_amount_price, average_price))
    cursor.execute(
        'INSERT OR REPLACE INTO reports_logistics (number, amount, average_price) VALUES (?,?,?)',
        (return_amount, return_amount_price, average_price_r))
    cursor.execute(
        'INSERT OR REPLACE INTO reports_other (fines, surchages, compensation) VALUES (?,?,?)',
        (fines, surchages, compensation))
    connection.commit()
    connection.close()