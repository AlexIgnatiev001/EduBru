d = {'name': 'id56', 'name1': 'id786', 'name2': 'id2'}

for k in d:
    d[d.pop(k)] = k
print(d)
