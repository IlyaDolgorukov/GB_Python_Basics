# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('02.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()

print(f'Всего строк: {len(text)}')
for num, line in enumerate(text):
    print(f'Строка: {num + 1}, Слов: {len(line.split())}')
