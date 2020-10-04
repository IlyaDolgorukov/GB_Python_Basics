# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_list = []
q = 'y'

while q != 'n':
    item = input('Введите значение элемента: ')
    user_list.append(item)
    q = input('Хотите продолжить? (y/n): ')

tmp_list = []
cnt = len(user_list)

print(f'Получился список из {cnt} элементов:')
print(user_list)

for ind in range(int(cnt / 2)):
    tmp_list.append(user_list.pop(ind))

tmp_list.reverse()

for ind in range(cnt):
    if ind % 2 != 0:
        user_list.insert(ind, tmp_list.pop())

print('После преобразования получилось: ')
print(user_list)
