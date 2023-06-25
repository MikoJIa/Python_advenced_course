# Сдвиг в развитии
# На вход программе подается строка текста из натуральных чисел.
# Из элементов строки формируется список чисел. Напишите программу циклического сдвига
# элементов списка направо, когда последний элемент становится первым,
# а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.
# Формат входных данных
# На вход программе подается строка текста из разделенных пробелами натуральных чисел.
# Формат выходных данных
# Программа должна вывести элементы измененного списка с циклическим сдвигом,
# разделяя его элементы одним пробелом.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 1 2 3 4 5
# Sample Output 1:
#
# 5 1 2 3 4
# Sample Input 2:
#
# 6 6 6 6 6 6 6
# Sample Output 2:
#
# 6 6 6 6 6 6 6
# Sample Input 3:
#
# 5 4 3 2 1
# Sample Output 3:
#
# 1 5 4 3 2
# Sample Input 4:
#
# 489 483 43 2 3 84 1 4 3 2 5 4 3 13
# Sample Output 4:
#
# 13 489 483 43 2 3 84 1 4 3 2 5 4 3


def shift_dev(num: list[int], steps=0) -> list[int]:
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            num.append(num.pop(0))
        return num
    else:
        for i in range(steps):
            num.insert(0, num.pop())
        return num


res = list(map(int, input().split()))
print(*shift_dev(res, steps=-2))