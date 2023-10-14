import requests
from bs4 import BeautifulSoup
pages = 3
l = []
for p in range(1, pages+1):
    url = 'https://www.nstu.ru/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    news = soup.find_all('div', class_='bottomLine')
    for n in news:
        url = n.select('a')[1]['href']
        id = int(url.split('=')[1])
        title = n.select('a')[1].text
        l.append({'id': id, 'title': title})
print(l)
input()
