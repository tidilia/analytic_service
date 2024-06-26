import requests
import openai
from openai import OpenAI, OpenAIError

# import { HttpsProxyAgent } from 'https-proxy-agent';

# new OpenAI({httpAgent: new HttpsProxyAgent(proxyUrl)});


def getProductData(productID):
    urls = {
        'content_get_cards_list': 'https://suppliers-api.wildberries.ru/content/v2/get/cards/list'
    }

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
    cards = response.json()['cards']
    res = []
    for i in cards:
        result = {}
        result['Наименование товара'] = i['title']
        result['Категория'] = i['subjectName']
        result['Бренд'] = i['brand']
        for j in i['characteristics']:
            result[j['name']] = j['value']
        res.append(result)

    return res


def makeDescription(productId, features):
    productData = getProductData(productId)[0]
    request = ('Создай продающее SEO-оптимизированное описание длиною в 2000 символов для товара ' +
               productData['Наименование товара'] +
               ' бренда ' + productData['Бренд'] +
               ' с категорией '
               + productData['Категория'])
    if features != "":
        request += '. Учитывай следующие особенности: ' + features
    print(request)
    client = openai.OpenAI(
        api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU4N2Q3MTA4LTJlMWUtNDJjOS04YWYxLTBlYTE5NDA2YzdlNCIsImlzRGV2ZWxvcGVyIjp0cnVlLCJpYXQiOjE3MTc2NzYxNDEsImV4cCI6MjAzMzI1MjE0MX0.0OVdh8tVnish8vT51WgBOIeCZBXurJoyE3myP6dS2iY',
        base_url='https://bothub.chat/api/v1/openai/v1'
    )
    try:
        chatAssistant = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Ты маркетолог, создающий описания товаров для продавцов на маркетплейсе. Постарайся использовать в описаниях большое количество ключевых запросов, подходящих для товара и учитвать seo-оптимизацию, создавай конкурентоспособные описания."
                },
                {
                    "role": "user",
                    "content": request
                }
            ],
            temperature=1,
            model="gpt-3.5-turbo-0613")
    except OpenAIError as e:
        result = f"Ошибка на сервере: {e}"
        return result
    result = ""
    if not chatAssistant.choices[0].message.content:
        result="Ошибка на сервере. Попробуйте повторить запрос позже."
    else:
        result=chatAssistant.choices[0].message.content
    return result


