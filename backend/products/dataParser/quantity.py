import requests
import datetime
import json
import environ

def update_database():
    env = environ.Env()
    # reading .env file
    environ.Env.read_env()
    api_key = env("WB_API")
    url = 'https://seller-analytics-api.wildberries.ru/api/v2/nm-report/detail'
    today = datetime.datetime.now().replace(microsecond=0) - \
        datetime.timedelta(hours=2)
    yesterday = (datetime.datetime.now().replace(
        microsecond=0) - datetime.timedelta(days=1))
    t = datetime.datetime.strftime(today, '%Y-%m-%d %H:%M:%S')
    y = datetime.datetime.strftime(yesterday, '%Y-%m-%d %H:%M:%S')

    p = {
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
    result = response.json()['data']['cards']
    for r in result:
        print(r['nmID'], ' ', r['stocks']['stocksWb'])


update_database()
