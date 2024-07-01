import requests
import datetime
import sqlite3
import environ



def update_database():
    urls = {
        'statistics_get_orders': 'https://statistics-api.wildberries.ru/api/v1/supplier/orders'}
    url = urls['statistics_get_orders']
    env = environ.Env()
    # reading .env file
    environ.Env.read_env()
    api_key = env("WB_API")
    db_path = env.db_url
    
    headers = {
        "Authorization": api_key
    }

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    today = datetime.datetime.now().replace(microsecond=0)
    last_week = (today.replace(microsecond=0) - datetime.timedelta(days=6))
    cursor.execute('SELECT date FROM productItemData_productDayOrders LIMIT 1')
    info = cursor.fetchone()
    if info != None:
        info = info[0]
        info = info[:10]
        if (info == datetime.datetime.strftime(today, '%Y-%m-%d')):
            print('already download')
            return

    tables = ['`productItemData_productDayOrders`',
              '`productItemData_productWeekOrders`']
    for t in tables:
        cursor.execute('DELETE FROM %s' % t)
    connection.commit()

    get_params = {
        "dateFrom": today,
        "flag": 1
    }

    response = requests.get(url, headers=headers, params=get_params)
    if (response.status_code != 200):
        print("dayError")
        print(response.text)
        return
    for i in response.json():
        date = i['date']
        time = int(date[11:13])
        size = i['techSize']
        print(size)
        week_time = int((datetime.datetime.strptime(
            date, '%Y-%m-%dT%H:%M:%S') - last_week).days)
        sku = i['barcode']
        nmID = i["nmId"]
        cursor.execute('INSERT OR REPLACE INTO productItemData_productDayOrders ( date, sku, nmID, time, size ) VALUES ( ?, ?, ?, ?, ?)',
                       (date, sku, nmID, time, size))
        cursor.execute('INSERT OR REPLACE INTO productItemData_productWeekOrders ( date, sku, nmID, time, size ) VALUES ( ?, ?, ?, ?, ? )',
                       (date, sku, nmID,  week_time, size))

    get_params = {
        "dateFrom": last_week,
        "flag": 0
    }
    response = requests.get(url, headers=headers, params=get_params)
    if (response.status_code != 200):
        print(response.text)
        return
    for i in response.json():
        date = i['date']
        week_time = int((datetime.datetime.strptime(
            date, '%Y-%m-%dT%H:%M:%S') - last_week).days)
        sku = i['barcode']
        nmID = i["nmId"]
        size = i['techSize']
        if (datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S') < today) and (datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S') > last_week):
            cursor.execute('INSERT OR REPLACE INTO productItemData_productWeekOrders ( date, sku, nmID, time, size ) VALUES ( ?, ?, ?, ?, ? )',
                           (date, sku, nmID, week_time, size))
    connection.commit()
    connection.close()


def get_real_price(nmID):
    print(nmID)
    urls = {
        'statistics_get_report': 'https://statistics-api.wildberries.ru/api/v5/supplier/reportDetailByPeriod'}
    url = urls['statistics_get_report']
    env = environ.Env()
    # reading .env file
    environ.Env.read_env()
    api_key = env("WB_API")

    headers = {
        "Authorization": api_key
    }
    today = datetime.datetime.now().replace(microsecond=0).isoformat()
    last_month = (today.replace(
        microsecond=0) - datetime.timedelta(days=30))
    t = datetime.datetime.strftime(today, '%Y-%m-%dT%H:%M:%S')
    m = datetime.datetime.strftime(last_month, '%Y-%m-%dT%H:%M:%S')

    get_params = {
        "dateFrom": m,
        "dateTo": t
    }

    response = requests.get(url, headers=headers, params=get_params)
    if (response.status_code != 200):
        print(response.text)
        return 
    result = response.json()

    delivery_amount = 0
    income = 0
    sales_count = 0

    for i in result:
        if (i['nm_id'] == nmID):
            supplier_oper_name = i['supplier_oper_name']
            if supplier_oper_name == 'Продажа':
                income += i['ppvz_for_pay']
                sales_count += 1
            elif supplier_oper_name == 'Логистика':
                delivery_amount += i['delivery_rub']

    if sales_count == 0:
        result = {
            'salesCount': 0,
            'month': 0,
            'item' : 0
        }
    else:
        result = {
            'salesCount': sales_count,
            'month' : income - delivery_amount,
            'item' : (income - delivery_amount) / sales_count
        }
    return result


    


def get_conversia(nmID):
    url = 'https://seller-analytics-api.wildberries.ru/api/v2/nm-report/detail'
    env = environ.Env()
    # reading .env file
    environ.Env.read_env()
    api_key = env("WB_API")
    today = datetime.datetime.now().replace(microsecond=0) - \
        datetime.timedelta(hours=2)
    yesterday = (datetime.datetime.now().replace(
        microsecond=0) - datetime.timedelta(days=30))
    t = datetime.datetime.strftime(today, '%Y-%m-%d %H:%M:%S')
    y = datetime.datetime.strftime(yesterday, '%Y-%m-%d %H:%M:%S')

    p = {
        "nmIDs": [nmID],
        "period": {
            "begin": y,
            "end": t
        },
        "page": 1
    }
    headers = {
        "Authorization": api_key
    }
    response = requests.post(url, json=p, headers=headers)
    if (response.status_code != 200):
        print(response.text)
        return
    result = response.json()[
        'data']['cards'][0]['statistics']['selectedPeriod']
    return_data = {}
    return_names = ['cancelCount', 'buyoutsCount',
                    'openCardCount', 'addToCartCount', 'ordersCount', 'ordersSumRub', 'buyoutsSumRub', 'cancelSumRub', 'avgPriceRub']
    for i in return_names:
        return_data[i] = result[i]
    return (return_data)
