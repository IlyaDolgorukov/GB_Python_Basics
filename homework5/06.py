# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

result = {}

with open('06.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()

for line in text:
    data = line.split()
    name = data.pop(0).replace(':', '')
    val = 0
    for part in data:
        num = part.split('(').pop(0)
        if num.isdigit():
            val += int(num)
    result[name] = val

print(result)
