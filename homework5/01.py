# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

result = []
stop = False

while not stop:
    string = input('Введите строку (либо пустая строка для завершения): ')
    if len(string) > 0:
        result.append(string)
    else:
        stop = True

with open('01.txt', 'w', encoding='utf-8') as file:
    for line in result:
        file.write(line + '\n')
