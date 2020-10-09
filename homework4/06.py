# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

from itertools import count, cycle

for i in count(3):
    print(i)
    if i == 10:
        break

cnt = 0
nums = ['one', 'two', 'three', 'four', 'five']
for i in cycle(nums):
    cnt += 1
    print(i)
    if cnt >= 10:
        break
