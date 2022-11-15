import requests


def currency_rates(CODE):
    respons = requests.get('https://www.cbr-xml-daily.ru/daily.xml')
    content = respons.text
    if respons.ok:
        curs = content.split(CODE)
        value = curs[1].split("</Value>")[0].split("<Value>")[1]
        value = float(value.replace(",", "."))
        date = respons.headers["Date"]

        return (f'курс в рублях за 1 единицу {CODE}: {value}', date)
    else:
        return None


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('AUD'))
#print(currency_rates('AZN'))




