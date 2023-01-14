from random import randint

n = 5
maximum = 0
m = [[randint(0, 100) for j in range(n)] for i in range(n)]
for i in range(n):
    print(*m[i])
    for j in range(n):
        if m[i][j] > maximum:
            maximum = m[i][j]
print('Максимальное значение: ', maximum)