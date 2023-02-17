import random


class Combatant:

    def __init__(self, name):
        self.health = 100
        self.end = 100
        self.armor = 100
        self.correction = 0
        self.name = name

    def assault(self, second, correction):
        print(f'{self.name}:')
        print(' ' * len(self.name), end='')
        print(f'выносливость {self.end} - 10 = {self.end - 10}')
        self.end -= 10
        if second == 'assault':
            tmp = random.randint(10, 30) - correction
            print(f'{" " * len(self.name)}здоровье {self.health} - {tmp} = {self.health - tmp}')
            self.health -= tmp

    def protect(self, second, correction):
        if second == 'assault':
            tmp1 = random.randint(0, 10) - correction
            tmp2 = random.randint(0, 20) + self.check_armor(self.armor) - correction
            print(f'{self.name}:')
            print(f'{" " * len(self.name)}броня {self.armor} - {tmp1} = {self.armor - tmp1}')
            print(f'{" " * len(self.name)}здоровье {self.health} - {tmp2} = {self.health - tmp2}')
            self.armor -= tmp1
            self.health -= tmp2

    def check_armor(self, arm):
        res = 0
        if arm <= 0:
            self.armor = 0
            res = 10
        return res

    def check_endu(self, end):
        if end <= 0:
            self.correction = random.randint(0, 10)

    def check_health(self):
        if self.health > 10:
            return True
        else:
            ask = input(f'{self.name}({self.health}) кончился, убить его?(да - 1/нет - 2)   ')
            if ask == '1':
                print('Убиваем')
            else:
                print('Пускай еще поживет')


Vasya = Combatant('Вася')
Petya = Combatant('Петя')

while Vasya.check_health() and Petya.check_health():
    v = random.choice(['protect', 'assault'])
    p = random.choice(['protect', 'assault'])
    print(f'Вася(здоровье {Vasya.health}) - {v}      Петя(здоровье {Petya.health}) - {p}')
    if v == 'assault':
        Vasya.assault(p, Petya.correction)
    else:
        Vasya.protect(p, Petya.correction)
    if p == 'assault':
        Petya.assault(v, Vasya.correction)
    else:
        Petya.protect(v, Vasya.correction)
    print()
