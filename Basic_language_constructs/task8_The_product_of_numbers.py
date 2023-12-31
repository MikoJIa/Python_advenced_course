# Напишите программу для определения, является ли число произведением двух чисел из
# данного набора, выводящую результат в виде ответа «ДА» или «НЕТ».
# Формат входных данных
# В первой строке подаётся число
# n(0<n<1000) – количество чисел в наборе. В последующих
# n строках вводятся целые числа, составляющие набор (могут повторяться).
# Затем следует целое число, которое является или не является произведением двух каких-то
# чисел из набора.
# Формат выходных данных
# Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.
# Примечание 1. Само на себя число из набора умножиться не может, другими словами,
# два множителя должны иметь разные индексы в наборе.
# Примечание 2. Для решения задачи используйте вложенные циклы.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 3
# 33
# 17
# 35
# 999
# Sample Output 1:
#
# НЕТ
# Sample Input 2:

# 4
# 89
# 4
# 77
# 4
# 16
# Sample Output 2:
#
# ДА


def product_of_numbers(n: int) -> str:
    ls = []
    if 0 < n < 1000:
        while len(ls) != n + 1:
            num = int(input())
            ls.append(num)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if i != j:
                if ls[i] * ls[j] == ls[-1]:
                    return 'ДА'
    return 'НЕТ'



print(product_of_numbers(int(input())))


# enother solution

size = int(input())
seq = [int(input()) for _ in range(size)]
number = int(input())
flag = False

for i in range(size):
    for j in range(size):
        if i != j and seq[i] * seq[j] == number:
            flag = True

if flag:
    print("ДА")
else:
    print("НЕТ")