# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def print_usr(name='Unknown', surname='Unknown', year='Unknown', city='Unknown', email='Unknown', phone='Unknown'):
    print(f'{name} {surname}, {year} г.р., проживает в г. {city}, email: {email}, тел.: {phone}')


print_usr(name='Иван', surname='Петров', year='1978', city='Сочи', email='vanya.pet@mail.ru', phone='8 (800) 345-15-10')
