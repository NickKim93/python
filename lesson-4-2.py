# 2. task 2
from requests import get


def currency_rates(cur):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.text
    for el in content.split('<CharCode>')[1:]:
        el = el.split('</CharCode>')[0]
        if el == cur:
            for cur in content.split(el)[1:]:
                cur = cur.split('<Value>')[1]
                print(cur.split('</Value>')[0])


currency_rates(input('Введите код валюты на англ языке: '))
