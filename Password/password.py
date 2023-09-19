import random
import os

name_account = str(input('Введите имя аккаунта : '))
len_password = int(input('Введите длину пароля : '))
new_password = ''.join(
    (random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_-+={}[]|') for i in
     range(len_password)))
f = open('password.txt', 'a+')
f.seek(0, 2)
f.write(name_account + ': ' + new_password + '\n')
f.close()
print('В файл добавлен новый пароль и сохранен !!!', '\n''Путь до файла: ', os.getcwd())
print(new_password)
