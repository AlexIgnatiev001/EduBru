x, y, p = int(input('Deposit:')), int(input('Target: ')), int(input('Percent/year: '))
years = 0
while x < y:
    x += x * p / 100
    years += 1
print(years)