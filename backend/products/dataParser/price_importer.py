import requests
import sqlite3
import datetime


def update_database():
    url = 'https://discounts-prices-api.wb.ru/api/v2/list/goods/filter'
    api_key = 'eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQwMjI2djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTcyODk0NTU5MSwiaWQiOiI3YThjNWM2OS02ZmQyLTQyMDYtOTJmYy0wZDk3Zjc2ZTNmMTEiLCJpaWQiOjU5MTY0MDE5LCJvaWQiOjExNjI3NzcsInMiOjQ0LCJzaWQiOiI5YzVhYjQ5MS1jNjkzLTQ1M2QtYjIxMC1jZmM3MzgyOWIwMjEiLCJ0IjpmYWxzZSwidWlkIjo1OTE2NDAxOX0.-_B3tBks_1q1OaTLs6JKewzsX5KcumxQygYDEJoWNRlUiv8TLKXwlBGgXR86kB9gsv9koh8Y0OYsnWE8v3T0OA'
    db_path = "/Users/dianahazgalieva/Desktop/analytic_service/backend/db.sqlite3"

    get_params = {
        "limit": '1000'
    }
    headers = {
        "Authorization": api_key,
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.get(url, get_params, headers=headers)
    result = response.json()["data"]['listGoods']

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    #print(result)
    for res in result:
        nmID = res['nmID']
        disc = res['discount']
        bool_edit_price = res['editableSizePrice']
        size_str = ""
        price_list = list()
        for i, s in enumerate(res['sizes']):
            if i != 0:
                size_str += ', '
            cursor.execute('UPDATE products_goods SET discount = ?, price = ?, discountedPrice = ?, editableSizePrice = ? WHERE size = ? AND product_id = ? ',
                           (disc, s['price'], s['discountedPrice'], bool_edit_price, s['techSizeName'], nmID))
            size_str += s['techSizeName']
            price_list.append(float(s['discountedPrice']))
        min_price = min(price_list)
        max_price = max(price_list)
        price_str = ""
        if min_price == max_price:
            price_str = str(min_price)
        else:
            price_str = min_price + ' - ' + max_price
        cursor.execute('UPDATE products_product SET sizes = ?, price = ? WHERE nmID = ?',
                       (size_str, price_str, nmID))

    connection.commit()
    connection.close()


