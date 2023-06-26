# На вход программе подается строка текста, содержащая натуральные числа,
# расположенные по неубыванию. Из строки формируется список чисел.
# Напишите программу для подсчета количества разных элементов в списке.
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа,
# разделенные символом пробела, расположенные по неубыванию.
# Формат выходных данных
# Программа должна вывести одно число – количество различных элементов списка.
# Примечание. Задачу можно решить без множеств.
# Тестовые данные 🟢
# Sample Input 1:
# 1 1 1 2 2 2 2 3 3 3
# Sample Output 1:
# 3


def various_elements(num: list[int]) -> int:
    count = 1
    for i in range(len(num)-1):
        if num[i] != num[i+1]:
            count += 1
        else:
            count = count
    return count


num = list(map(int, input().split()))
print(various_elements(num))


def func(num):
    if sum(num) >= 0:
        return len(set(num))
    elif num is []:
        return None


num = list(map(int, input().split()))
print(func(num))