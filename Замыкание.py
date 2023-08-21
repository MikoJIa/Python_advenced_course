# def main_func(name):
#     def inner_func():
#         print('Hello my friend', name)
#
#     return inner_func
#
#
# d = main_func('Kolya')
# d()  # Hello my friend Kolya
#
#
# def adder(value):
#
#     def inner(a):
#         return value + a
#
#     return inner
#
#
# c = adder(10)
# print(c(5))  # 15
#
#
# def counter():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner
#
#
# f = counter()
# print(f())
# print(f())
# print(f())
#
#
# def everage_numbers():
#     numbers = []
#
#     def inner(number):
#         numbers.append(number)
#         print(numbers)
#         return sum(numbers) / len(numbers)
#     return inner
#
#
# d = everage_numbers()
# print(d(10))
# print(d(5))
# print(d(5))
# print(d(5))
# print(d(5))
#
#
# def aver_numbers():
#     summa = 0
#     count = 0
#     res_lst = []
#
#     def inner(num):
#         nonlocal summa
#         nonlocal count
#         summa += num
#         count += 1
#         res_lst.append(summa / count)
#         return res_lst
#     return inner
#
#
# g = aver_numbers()
# print(g(10))
# print(g(5))
# print(g(5))
# print(g(2))
import time
from datetime import datetime
from time import perf_counter
from time import sleep


# def timer():
#     count = 0
#     start = time.time()
#     for j in range(1, 100000000, 1):
#         count += (j ** 2)
#     finish = time.time()
#     def inner():
#         res = finish - start
#         print(f'{res} sec')
#         return res
#     return inner
#
#
# c = timer()
# c()


def square_triangle(func):

    def inner(*args, **kwargs):
        s = func(*args, **kwargs)
        res = s / 2
        print(f'Площадь треугольника равна {res}')
    return inner


@square_triangle
def calculater(a, b, c):
    res = a + b + c
    return res


calculater(2, 3, 2)
