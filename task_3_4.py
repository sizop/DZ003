# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
#
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

import random, math


def list_rnd(num):
    my_list = [round(random.uniform(-99.999, 100), 2) for my_list in range(num)]
    out_list = []
    for i in range(num):
        out_list.append(float('{:.3f}'.format(my_list[i] - math.trunc(my_list[i]))))
    print(my_list)
    return out_list


list_1 = list_rnd(int(input('Введите количество элементов: ')))
print(f'min number: {min(list_1)} \nmax number: {max(list_1)}')
