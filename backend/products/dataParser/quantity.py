import requests
import datetime
import json


def update_database():
    url = 'https://seller-analytics-api.wildberries.ru/api/v2/nm-report/detail'
    api_key = 'eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQwMjI2djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTcyODk0NTU5MSwiaWQiOiI3YThjNWM2OS02ZmQyLTQyMDYtOTJmYy0wZDk3Zjc2ZTNmMTEiLCJpaWQiOjU5MTY0MDE5LCJvaWQiOjExNjI3NzcsInMiOjQ0LCJzaWQiOiI5YzVhYjQ5MS1jNjkzLTQ1M2QtYjIxMC1jZmM3MzgyOWIwMjEiLCJ0IjpmYWxzZSwidWlkIjo1OTE2NDAxOX0.-_B3tBks_1q1OaTLs6JKewzsX5KcumxQygYDEJoWNRlUiv8TLKXwlBGgXR86kB9gsv9koh8Y0OYsnWE8v3T0OA'
    db_path = "/Users/dianahazgalieva/Desktop/analytic_service/backend/db.sqlite3"
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
