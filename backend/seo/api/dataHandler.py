import requests

def getProductData(productID):
    urls = {
        'content_get_cards_list': 'https://suppliers-api.wildberries.ru/content/v2/get/cards/list'
    }
    db_path = "/Users/dianahazgalieva/Desktop/analytic_service/backend/db.sqlite3"

    url = urls['content_get_cards_list']
    content_api_key = "eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQwMjI2djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTcyOTA0MDMwMSwiaWQiOiJhYWFhZTcyZC01OTIyLTRkMjItOTdlMi1hYzZkOGQwYjZkYjMiLCJpaWQiOjU5MTY0MDE5LCJvaWQiOjExNjI3NzcsInMiOjEwNzM3NDE4MjYsInNpZCI6IjljNWFiNDkxLWM2OTMtNDUzZC1iMjEwLWNmYzczODI5YjAyMSIsInQiOmZhbHNlLCJ1aWQiOjU5MTY0MDE5fQ.PFP0UeHJ9fNXSO-IdR-JojPo-LCn0dYWlfTuZ01ofMspau0c4wvQSVno6lhRflO-c41IxiorU5s7z6d3EW-3Aw"

    headers = {
        "Authorization": content_api_key
    }

    i = '"' + str(productID) + '"'
    body = f'''
            {{
              "settings": {{
                "cursor": {{
                  "limit": 100
              }},
              "filter": {{
                "withPhoto": -1,
                "textSearch": {i}
                }}
              }}
            }}
            '''
    response = requests.post(url, headers=headers, data=body)
    print(response.text)
    return response.text


def makeDescription(id, amount, features):
    getProductData(id)
    return ""
