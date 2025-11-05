# Homework
# Задоянная Анастасия, Дубина Александра БИ-252
import requests
from bs4 import BeautifulSoup


def getrates():
    try:
        url = 'https://cbr.ru/currency_base/daily/'
        response = requests.get(url)


        soup = BeautifulSoup(response.content, 'html.parser')
        rates = {'RUB': 1.0}

        # Ищем в тексте таблицу с курсами валют
        currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CNY', 'CHF', 'CAD', 'AUD']

        table = soup.find('table', class_='data')
        if table:
            rows = table.find_all('tr')
            for row in rows[1:]:
                cols = row.find_all('td')
                if len(cols) >= 5:
                    currcode = cols[1].text.strip() #извлекаем код валюты
                    value = cols[4].text.strip().replace(',', '.') #преобразовываем число в нужный тип для питона
                    # Добавляем только если валюта в нашем списке
                    if currcode in currencies and value:
                        try:
                            rates[currcode] = float(value) #текст в число
                        except ValueError:
                            continue


        return rates
    except Exception as e:
        print(f'ERROR: {e}')
        return None


if __name__ == '__main__':
    rates = getrates()
    if rates:
        for curr, rate in rates.items():
            pass
