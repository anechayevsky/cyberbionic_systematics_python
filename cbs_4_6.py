login = 'login'
password = 'password'
for attempt in range(3):
    new_login = input('Введіть ваш логін: ')
    new_password = input('Введіть ваш пароль: ')
    if new_login == login and new_password == password:
        print(f'Авторизацію успішно пройдено з {attempt+1} спроби')
        break
    else:
        print(f'Спробуйте ще раз. Залишилось {3-(attempt+1)} спроби')