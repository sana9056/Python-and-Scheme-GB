""" 1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python и разрядность
вашей ОС. """

import sys

""" HomeWork1_1"""


number = input('Введите число: ')

sum = 0
prod = 1

for f in number:
    sum += int(f)
    prod *= int(f)
print(f"Сумма цифр числа {number}: {sum}")
print(f"Произведение цифр: {number}: {prod}")

sum_size = 0
sum_size += sys.getsizeof(number)
sum_size += sys.getsizeof(sum)
sum_size += sys.getsizeof(prod)

print('Переменные занимают', sum_size)


'''
x64_Win10
Python 3.8
'''


'''
Переменная занимает 107 бит
'''
