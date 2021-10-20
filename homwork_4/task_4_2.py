import requests

def currency_rates(currency_designation):

    currency_designation = currency_designation.upper()
    r = requests.request('get', 'http://www.cbr.ru/scripts/XML_daily.asp')
    paragraph = r.text.split('Valute')
    exchange_rates = {}

    for i in range(1, len(paragraph)-1, 2):
        line = paragraph[i].split('><')
        char_code = line[2]
        value = line[5]
        currency_1 = char_code.split('>')
        currency_1_1 = currency_1[1].split('<')
        currency = currency_1_1[0]
        meaning_1 = value.split('>')
        meaning_1_1 = meaning_1[1].split('<')
        meaning = meaning_1_1[0]
        exchange_rates.setdefault(currency, meaning)

        a = exchange_rates.get(currency_designation, None)

    date_1 = paragraph[0].split('"')
    date = date_1[5]

    return f"{a}, {date}"


print(currency_rates('usd'))
