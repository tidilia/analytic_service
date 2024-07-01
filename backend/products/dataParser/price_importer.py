import requests
import sqlite3
import datetime
import environ

def update_database():
    env = environ.Env()
    # reading .env file
    environ.Env.read_env()
    db_path = env("DB_PATH")
    api_key = env("WB_API")

    url = 'https://discounts-prices-api.wb.ru/api/v2/list/goods/filter'

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


