lst = [1, 2, 3, 1, 3, 'hi', 2]
uniq = []
double = []
for c in lst:
    if c not in uniq:
        uniq.append(c)
    else:
        double.append(c)
print(*double)