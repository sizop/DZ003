# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
#
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
#
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def fib(num):
    num_fib = [-1, 0, 1]
    num_fib_revers = []
    for i in range(2, num + 1):
        num_fib.append(num_fib[i] + num_fib[i - 1])
        num_fib_revers.insert(0, (num_fib[i] + num_fib[i - 1]) * (-1))
    num_fib = num_fib_revers + num_fib
    return num_fib


print(fib(int(input('Задайте число: '))))

# def fibonacci(n):
#     if (n <= 1):
#         return n
#     else:
#         return (fibonacci(n-1) + fibonacci(n-2))
# n = int(input("Введите число членов последовательности:"))
# print("Последовательность Фибоначчи:")
# for i in range(n+1):
#     print(fibonacci(i),end=' ')
