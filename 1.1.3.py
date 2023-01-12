a, b = int(input()), int(input())
maximum = (a > b) * a + (a < b) * b
print(maximum)