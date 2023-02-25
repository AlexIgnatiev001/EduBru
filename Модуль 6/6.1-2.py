import time
from threading import Thread
from datetime import datetime


def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)


def in_series(names):
    for name in names:
        get_thread(name)


def parallel(names):
    threads = [Thread(target=get_thread, args=(i,)) for i in names]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def timing(names, way):
    t1 = datetime.now()
    way(names)
    t2 = (datetime.now() - t1).seconds
    print(f'Time: {t2} sec.')
    return t2


names = ['abc', 'def', 'ghi', 'xyz', 'utp']
t3 = timing(names, in_series) - timing(names, parallel)
print(f'Разница во времени составила:{t3} сек.')
