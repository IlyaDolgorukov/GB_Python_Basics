# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько
# чисел и строк и сохраните в переменные, выведите на экран.

x = 10
y = 10.45
z = True
hello = 'Hello world!'

print(type(x), x)
print(type(y), y)
print(type(z), z)
print(type(hello), hello)

name = input('Как вас зовут? ')
age = int(input('Сколько вам лет? '))
profession = input('Кем вы работаете? ')

print(f'{name=}; {age=}; {profession=};')
