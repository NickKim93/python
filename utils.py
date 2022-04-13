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
    else:
        print('Wrong format please re-enter the ')


if __name__ == '__main__':
    currency_rates(input('Введите код валюты на англ языке: '))

