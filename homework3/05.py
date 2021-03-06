# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
# сумме и после этого завершить программу.

result = 0
stop = False

while not stop:
    string = input('Введите числа, разделенные пробелом (для завершения введите Q): ')
    arr = string.split()
    for item in arr:
        if item.lower() == 'q':
            stop = True
            break
        else:
            result += int(item)
    print(f'Результат сложения всех чисел: {result}')
