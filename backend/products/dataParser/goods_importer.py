import requests
import sqlite3
import environ

def update_database():
    urls = {
        'content_get_cards_list': 'https://suppliers-api.wildberries.ru/content/v2/get/cards/list'
    }
    env = environ.Env()
    # reading .env file
    environ.Env.read_env()
    db_path = env("DB_PATH")

    url = urls['content_get_cards_list']
    content_api_key = env("WB_API_content")

    headers = {
        "Authorization": content_api_key
    }

    body = '''{
              "settings": {
                "cursor": {
                  "limit": 100
              },
              "filter": {
                "withPhoto": -1
                }
              }
            }'''
    response = requests.post(url, headers=headers, data=body)
    if (response.status_code != 200):
        print(response.text)
        return
    result = (response.json())['cards']
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    for res in result:
        imtID = int(res["imtID"])
        name = res["title"]
        nmID = int(res["nmID"])
        vendorCode = res["vendorCode"]
        brand = res["brand"]
        category = res["subjectName"]
        image = res["photos"][0]['c246x328']
        cursor.execute(
            'SELECT quantity FROM products_product WHERE nmID = ?', (nmID,))
        existing_item = cursor.fetchone()
        if not existing_item:
            existing_item = list()
            existing_item.append(0)
        cursor.execute('INSERT OR REPLACE INTO products_product (name, nmID , vendorCode, imtID, brand, category, quantity, photo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                       (name, nmID, vendorCode, imtID, brand, category, existing_item[0], image))
        for obj in res["sizes"]:
            imtID = int(res["imtID"])
            nmID = int(res["nmID"])
            vendorCode = res["vendorCode"]
            size = obj["techSize"]
            sku = obj["skus"][0]
            product = nmID
            cursor.execute(
                'SELECT inWayToClient, inWayFromClient, quantityFull, quantity FROM products_goods WHERE sku = ?', (sku,))
            existing_obj = cursor.fetchone()
            if not existing_obj:
                existing_obj = (0, 0, 0, 0)
            inWayToClient, inWayFromClient, quantityFull, quantity = existing_obj
            cursor.execute('INSERT OR REPLACE INTO products_goods ( vendorCode,  imtID , size, sku, product_id, inWayToClient, inWayFromClient, quantityFull, quantity, discount, discountedPrice, price, editableSizePrice, photo) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                           (vendorCode,  imtID, size, sku, product, inWayToClient, inWayFromClient, quantityFull, quantity, 0, 0, 0, False, image))

    connection.commit()
    connection.close()



