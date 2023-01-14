import json
#Регистрация пользователя с проверкой наличия логина в базе
def register(login, passwd):
    with open('users.json', 'r') as file:
        users = json.load(file)
    if login not in users:
        users[login] = passwd
        with open('users.json', 'w') as file:
            json.dump(users, file)
    else:
        print('Такой логин уже существует')
        register(input('Введите логин: '), input('Введите пароль: '))

#Логин
def check(login, passwd):
    with open('users.json', 'r') as file:
        users = json.load(file)
    if login not in users.keys():
        print('Пользователя с таким логином не существует')
        check(input('Введите логин: '), input('Введите пароль: '))
    if users[login] == passwd:
        print('Вы вошли в систему')
    else:
        check(login, input('Неверный пароль, повторите: '))


def welcome():
    choise = int(input('Для регистрации наберите 1, для входа в систему - 2: '))
    if choise == 1:
        register(input('Введите логин: '), input('Введите пароль: '))
    elif choise == 2:
        check(input('Введите логин: '), input('Введите пароль: '))
    else:
        print('Повторите ввод')
        welcome()


print('Добро пожаловать!')
welcome()
