lst1 = sorted([2, 54, 43, 12, 11, 67, 32, 17, 19, 27, 29, 31])


# Функция бинарного поиска принимает на вход список, искомое число и границы области поиска
def bi_search(lst, num, llimit, rlimit):
    median = llimit + (rlimit - llimit) // 2
    if num == lst[median]:
        return median
    elif num < lst[median]:
        return bi_search(lst, num, llimit, median - 1)
    else:
        return bi_search(lst, num, median + 1, rlimit)


for i in lst1:
    print(f'Позиция {i} в списке - {bi_search(lst1, i, 0, len(lst1) - 1)}')
