pw = ''
big, small = False, False
while len(pw) < 8 or not big or not small:
    pw = input('Input password: ')
    for c in pw:
        if c.islower():
            small = True
        elif c.isupper():
            big = True
        if small == True & big == True:
            break
print('Good pass:', pw)