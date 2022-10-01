# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
#
# out
# [10, 2, 3, 8, 9]
# 22
#
# in
# 4
#
# out
# [4, 2, 4, 9]
# 8

from random import sample, randint
def create_new_list(num):
    if num < 0:
        return "Negative value of the number of numbers!"
    list_num = sample(range(1, num * 2), num)
    print(list_num)
    return list_num
print(sum(create_new_list(int(input('Количество чисел:')))[::2]))
