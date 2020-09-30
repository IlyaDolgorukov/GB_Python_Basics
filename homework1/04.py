# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = int(input('Введите число: '))
digit = result = 0

while num >= 1:
    digit = int(num % 10)
    result = max(digit, result)
    num = int(num / 10)

print(f'Наибольшая цифра в числе: {result}')
