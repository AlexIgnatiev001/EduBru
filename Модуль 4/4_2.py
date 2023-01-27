lst = [2, 54, 43, 12, 11, 67, 32, 17, 19, 27, 29, 31]

for i in range(1, len(lst)):
    x = lst[i]
    j = i
    while j > 1 and x < lst[j - 1]:
        lst[j], lst[j - 1] = lst[j - 1], lst[j]
        j -= 1
print(lst)
