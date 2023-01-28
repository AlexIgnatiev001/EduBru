lst1 = sorted([2, 54, 43, 12, 11, 67, 32, 17, 19, 27, 29, 31])


# Проверяем наличие искомого числа в списке
def check_num(lst, num):
    return num in lst


# Функция бинарного поиска принимает на вход список, искомое число и границы области поиска
def bi_search(lst, num, llimit, rlimit):
    median = llimit + (rlimit - llimit) // 2

    if num == lst[median]:
        return median
    elif num < lst[median]:
        return bi_search(lst, num, llimit, median - 1)
    else:
        return bi_search(lst, num, median + 1, rlimit)


x = int(input('Какое число следует найти в заданном списке?   '))
if check_num(lst1, x):
    print(f'Позиция числа {x} в списке - {bi_search(lst1, x, 0, len(lst1) - 1)}')
else:
    print('Это число отсутствует')