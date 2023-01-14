s = '''Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого...
...
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!'''

def len_less(s):
    result = []
    for word in s.split():
        word = word.strip(',.-;:!/')
        if len(word) < 5:
            result.append(word)
    return result
print(*len_less(s))