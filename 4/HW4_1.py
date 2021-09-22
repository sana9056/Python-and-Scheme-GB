# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках домашнего задания первых трех уроков.

# Создание матрицы

import random

import time

# Метод для будущего обрезания кол-ва цифр после запятой.


def tofixed(numobj, digits=0):
    return f"{numobj:.{digits}f}"
# --------------------------------------------------------------------------------------
#  №1 создание матрицы двумя циклами


start_time = time.time()


def m_create_2_for(range_raw, range_coll):
    matrix = [[random.randint(1, 100) for _ in range(1, range_coll)] for _ in range(1, range_raw)]
    # print(matrix)


m_create_2_for(1000, 1000)
time1 = time.time() - start_time
print("--- %s Секунд выполняется пример №1 ---" % (time.time() - start_time))

# --------------------------------------------------------------------------------------
# №2 Создание матрицы 1 циклом

start_time = time.time()


def m_create_1_for(size_matrix):
    matrix = []
    temp_array = []

    for i in range(1, (size_matrix ** 2) + 1):
        val = random.randint(1, 100)

        if i % size_matrix == 0:
            temp_array.append(val)
            matrix.append(temp_array)
            temp_array = []
        else:
            temp_array.append(val)
    # print(matrix)


m_create_1_for(1000)
time2 = time.time() - start_time
print("--- %s Секунд выполняется пример №2 ---" % (time.time() - start_time))

if time2 > time1:
    print("Пример 2 медленнее Примера 1 на ", tofixed(time2 - time1, 3), " секунд. И значит Пример 1 легче.")
else:
    print("Пример 1 медленнее Примера 2 на ", tofixed(time1 - time2, 3), " секунд. И значит Пример 2 легче.")
