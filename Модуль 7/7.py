import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests


url = 'https://mfd.ru/currency/?currency=USD'
req = requests.get(url)
src = req.text
soup = BeautifulSoup(src, 'lxml')

table = soup.find(class_='mfd-table mfd-currency-table').find_all('tr')[:0:-1]

exchange_dict = {}
for item in table:
    one_date = item.find_all('td')

    date = one_date[0].text[2:]
    rate = float(one_date[1].text)
    exchange_dict[date] = rate
print(exchange_dict)

x = [k for k in exchange_dict.keys()]
y = [v for v in exchange_dict.values()]
plt.tick_params(axis='x', which='major', labelsize=3, rotation=45)
plt.plot(x, y)
plt.show()
