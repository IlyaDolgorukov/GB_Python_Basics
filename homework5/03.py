# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

salary = []

with open('03.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()

print('У этих ребят маленькая зарплата:')

for line in text:
    n, s = line.split()
    salary.append(float(s))
    if float(s) < 20000:
        print(f'{n}: {s}')

print(f'Средняя зарплата в команде: {round((sum(salary) / len(salary)), 1)}')