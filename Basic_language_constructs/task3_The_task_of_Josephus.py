# n человек, пронумерованных числами от 1 до n < стоят в кругу. Они начинают считаться,
# каждый
# k-й по счету человек выбывает из круга, после чего счет продолжается со следующего за
# ним человека. Напишите программу, определяющую номер человека, который останется в кругу
# последним.
# Формат входных данных
# На вход программе подаются два числа n и k, записанные на отдельных строках.
# Формат выходных данных
# Программа должна вывести одно число – номер человека, который останется в кругу последним
# Примечание 1. Подробнее ознакомиться с классической задачей Иосифа Флавия можно тут.
# Примечание 2. Визуализацию работы алгоритма можно посмотреть тут.
# Тестовые данные 🟢
# Sample Input 1:
#
# 2
# 1
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# 5
# 2
# Sample Output 2:
#
# 3
# Sample Input 3:
#
# 7
# 5
# Sample Output 3:
#
# 6

# def josephus(n: int, k: int) -> int:
#     res = 0 if n == 0 else (josephus(n - 1, k) + k - 1) % n + 1
#     return res
#
#
# n = int(input())
# k = int(input())
# print(josephus(n, k))


# another solution

# def josephus(n, k):
#     count = 0
#     for i in range(1, n + 1):
#         count = count + k % i
#     print(k + 1)
#
#
# josephus(5, 2)
# n = 5
# k = 2
# list = [x for x in range(1, n + 1)]
# print(list)
# while len(list) != 1:
#     for i in range(0, k - 1):
#         print(i)
#         list.append(list[i])
#     del list[0:k]
#
# print(list)


def josephus(n, k):
    res = [x for x in range(1, n + 1)]
    while len(res) > 1:
        kill = k
        if k > len(res):
            if k % len(res) != 0:
                kill = k % len(res)
            else:
                kill = len(res)
        res = res[kill:] + res[:kill - 1]
    return res


# n = int(input())
# k = int(input())
print(*josephus(5, 2))