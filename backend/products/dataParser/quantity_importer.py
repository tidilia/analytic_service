# UPDATE books SET auth_id = 4 WHERE title = 'Белый клык';
# UPDATE products_GoodsQuantityAndPrice SET price = discount = WHERE sku =

import requests
import sqlite3
import datetime


def update_database():
    url = 'https://statistics-api.wildberries.ru/api/v1/supplier/stocks'
    api_key = 'eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQwMjI2djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTcyODk0NTU5MSwiaWQiOiI3YThjNWM2OS02ZmQyLTQyMDYtOTJmYy0wZDk3Zjc2ZTNmMTEiLCJpaWQiOjU5MTY0MDE5LCJvaWQiOjExNjI3NzcsInMiOjQ0LCJzaWQiOiI5YzVhYjQ5MS1jNjkzLTQ1M2QtYjIxMC1jZmM3MzgyOWIwMjEiLCJ0IjpmYWxzZSwidWlkIjo1OTE2NDAxOX0.-_B3tBks_1q1OaTLs6JKewzsX5KcumxQygYDEJoWNRlUiv8TLKXwlBGgXR86kB9gsv9koh8Y0OYsnWE8v3T0OA'
    db_path = "/Users/dianahazgalieva/Desktop/analytic_service/backend/db.sqlite3"
    offset = 200
    skip = 0

    get_params = {
        "skip": skip,
        "take": offset,
        "dateFrom": '2022-12-01'
    }
    headers = {
        "Authorization": api_key,
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.get(url, get_params, headers=headers)
    result = response.json()

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    for res in result:
        sku = res["barcode"]
        changeDate = res["lastChangeDate"]
        warehouse = res["warehouseName"]
        inWayToClient = res["inWayToClient"]
        inWayFromClient = res["inWayFromClient"]
        quantityFull = res["quantityFull"]
        quantity = res["quantity"]
        cursor.execute(
            'SELECT * FROM products_WarehouseData WHERE sku_id = ? AND warehouseName = ?', (sku, warehouse))
        item = cursor.fetchone()
        cursor.execute(
            'SELECT inWayToClient, inWayFromClient, quantityFull, quantity, product_id FROM products_Goods WHERE sku = ?', (sku,))
        goods = cursor.fetchone()
        if not item:
            cursor.execute('INSERT INTO products_WarehouseData (warehouseName, sku_id, lastChangeDate, inWayToClient, inWayFromClient, quantityFull, quantity) VALUES ( ?, ?, ?, ?, ?, ?, ?)',
                           (warehouse, sku, changeDate, inWayToClient, inWayFromClient, quantityFull, quantity))
            cursor.execute('UPDATE products_Goods SET inWayToClient = ?, inWayFromClient = ?, quantityFull = ?, quantity = ? WHERE sku = ?',
                           (goods[0] + inWayToClient, goods[1]+inWayFromClient, goods[2]+quantityFull, goods[3]+quantity, sku))
            cursor.execute('SELECT quantity, name FROM products_Product WHERE nmID = ?', (goods[4], ))
            q, name = cursor.fetchone()
            cursor.execute(
                'UPDATE products_Product SET quantity = ? WHERE nmID = ?', (q+quantityFull, goods[4]))
        else:
            changeDate_ = datetime.datetime.strptime(
                changeDate, "%Y-%m-%dT%H:%M:%S")
            lastDate = datetime.datetime.strptime(item[2], "%Y-%m-%dT%H:%M:%S")
            if changeDate_ > lastDate:
                print('change')
                inWayToClient = inWayToClient - item[3]
                inWayFromClient = inWayFromClient - item[4]
                quantityFull = quantityFull - item[5]
                quantity = quantity - item[6]
                cursor.execute('UPDATE products_WarehouseData SET inWayToClient = ?, inWayFromClient = ?, quantityFull = ?, quantity = ?, lastChangeDate = ? WHERE sku_id = ? AND warehouseName = ?',
                               (inWayToClient, inWayFromClient, quantityFull, quantity, changeDate, sku, warehouse))
                cursor.execute('UPDATE products_Goods SET inWayToClient = ?, inWayFromClient = ?, quantityFull = ?, quantity = ? WHERE sku = ?',
                               (goods[0] + inWayToClient, goods[1]+inWayFromClient, goods[2]+quantityFull, goods[3]+quantity, sku))
                cursor.execute(
                    'SELECT quantity FROM products_Product WHERE nmID = ?', (goods[4],))
                q = cursor.fetchone()[0]
                cursor.execute(
                    'UPDATE products_Product SET quantity = ? WHERE nmID = ?', (q + quantityFull, goods[4]))

    connection.commit()
    connection.close()