a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    x = 3
elif a == b or b == c or a == c:
    x = 2
else:
    x = 0
print(x)