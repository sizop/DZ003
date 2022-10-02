# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
#
# out
# [2, 5, 8, 10]
# [20, 40]
#
# in
# 5
#
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
from function import cr_nln


def out(my_list):
    out_list = []
    for i in range((len(my_list)) // 2):
        out_list.append(my_list[i] * my_list[-i - 1])
    if (len(my_list)) % 2:
        out_list.append(my_list[len(my_list) // 2])
    return out_list


my_list = cr_nln(int(input('Введите количество элементов: ')))
print(f'{my_list} \n {out(my_list)}')
