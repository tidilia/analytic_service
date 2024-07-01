import requests
import openai
from openai import OpenAI, OpenAIError
import environ


def getProductData(productID):
    urls = {
        'content_get_cards_list': 'https://suppliers-api.wildberries.ru/content/v2/get/cards/list'
    }

    url = urls['content_get_cards_list']
    env = environ.Env()
    # reading .env file
    environ.Env.read_env()
    content_api_key = env("WB_API_content")

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
    
    env = environ.Env()
    # reading .env file
    environ.Env.read_env()
    bothub_api_key = env("bothub_api_key")

    client = openai.OpenAI(
        api_key=bothub_api_key,
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


