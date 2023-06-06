# Дано пятизначное или шестизначное натуральное число. Напишите программу,
# которая изменит порядок его последних пяти цифр на обратный.
# Формат входных данных
# На вход программе подается одно натуральное пятизначное или шестизначное число.
# Формат выходных данных
# Программа должна вывести число, которое получится в результате разворота,
# указанного в условии задачи. Число нужно выводить без незначащих нулей.
# Тестовые данные 🟢
# Sample Input 1:
# 12345
# Sample Output 1:
# 54321
# Sample Input 2:
# 987654
# Sample Output 2:
# 945678
# Sample Input 3:
# 25000
# Sample Output 3:
# 52
# Sample Input 4:
# 560000
# Sample Output 4:
# 500006

def revers_num(num):
    length = len(num)
    l = []
    if length <= 5:
        for i in range(len(num)):
            if num[i] != 0:
                l.append(int(num[i]))
        print(*l[::-1], sep='')
    elif length > 5:
        for j in range(len(num)):
            l.append(num[j])
        l.append(num[0])
        print(*l[-6:][::-1], sep='')


num = list(map(int, input()))
revers_num(num)


#another solution

def revers_num(num):
    length = len(num)
    l = []
    if length <= 5:
        for i in range(len(num)):
            if num[i] != 0:
                l.append(int(num[i]))
        return l[::-1]
    elif length > 5:
        for j in range(1, len(num)):
            l.append(num[j])
        l.append(num[0])
        return l[::-1]

# another solution

num = list(map(int, input()))
print(*revers_num(num), sep='')


def func(num: int)-> int:
    if len(num) <= 5:
        print(int(num[::-1]))
    if len(num) > 5:
        print(num[0], num[:0:-1], sep='')


num = input()
func(num)
