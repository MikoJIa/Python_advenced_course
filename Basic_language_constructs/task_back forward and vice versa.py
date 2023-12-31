# На вход программе подается строка текста из натуральных чисел.
# Из элементов строки формируется список чисел. Напишите программу,
# которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
# Если в списке нечетное количество элементов, то последний остается на своем месте.
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные
# пробелами.
# Формат выходных данных
# Программа должна вывести измененный список, разделяя его элементы одним пробелом.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 1 2 3 4 5
# Sample Output 1:
#
# 2 1 4 3 5
# Sample Input 2:
#
# 2 3 2 4
# Sample Output 2:
#
# 3 2 4 2
# Sample Input 3:
#
# 1
# Sample Output 3:
#
# 1
import re

def vice_versa(num) -> int:
    lst = ''
    i = 0
    num = [int(x) for x in num]
    if len(num) % 2 == 1:
        while i != len(num[:-1]):
            num[i], num[i+1] = num[i+1], num[i]
            i += 2
        lst = num
    elif len(num) % 2 == 0:
        while i != len(num):
            num[i], num[i + 1] = num[i + 1], num[i]
            i += 2
        lst = num
    elif num:
        return lst
    return lst


num = input().split()
print(*vice_versa(num))

# another solution

s = list(map(int, input().split()))
s[:-1:2], s[1::2] = s[1::2], s[:-1:2]
print(*s)