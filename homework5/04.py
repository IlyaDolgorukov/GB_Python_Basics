# Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

nums = ['Один', 'Два', 'Три', 'Четыре']
result = []

with open('04.en.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()

for line in text:
    s, i = line.split(' - ')
    result.append(line.replace(s, nums[int(i) - 1]))

with open('04.ru.txt', 'w', encoding='utf-8') as file:
    file.writelines(result)
