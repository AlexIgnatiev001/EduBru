from threading import Thread
from datetime import datetime
import requests


def get_html(link):
    response = requests.get(link)
    print(link, response.ok)


def in_series(links):
    for link in links:
        get_html(link)


def parallel(links):
    threads = [Thread(target=get_html, args=(i,)) for i in links]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def timing(way, links):
    t1 = datetime.now()
    way(links)
    t2 = (datetime.now() - t1).microseconds / 1000000
    return t2


urls = ['https://www.python.org',
        'https://python.ru/',
        'https://pythonworld.ru',
        'https://ru.wikipedia.org/wiki/Python',
        'https://habr.com/ru/hub/python/'
        ]

t3 = timing(in_series, urls) - timing(parallel, urls)
if t3 < 0:
    print(f'Последовательный запуск быстрее параллельного на {-t3} сек')
else:
    print(f'Параллельный запуск быстрее последовательного на {t3} сек')
