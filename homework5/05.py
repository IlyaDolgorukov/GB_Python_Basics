# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

result = []
stop = False

while not stop:
    string = input('Введите число (либо пустая строка для завершения): ')
    if len(string) > 0:
        result.append(string)
    else:
        stop = True

with open('05.txt', 'w', encoding='utf-8') as file:
    file.write(' '.join(result))

with open('05.txt', 'r', encoding='utf-8') as file:
    text = file.read().split()

print(f'Сумма чисел в файле равна: {sum(map(lambda x: int(x), text))}')
