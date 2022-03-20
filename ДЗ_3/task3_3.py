# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random


def min_n(a: int, b: int):
    return a if a < b else b


def max_n(a: int, b: int):
    return a if a > b else b


def add_nums(a: int, b: int):
    return a + b


arr = [random.randint(0, 20) for i in range(10)]
print(arr)
max_num = arr[0]
min_num = arr[0]
sum_num = 0

for i in arr:
    min_num = min_n(min_num, i)
    max_num = max_n(max_num, i)


arr.remove(min_num)
arr.remove(max_num)

for i in arr:
    sum_num = add_nums(i, sum_num)

print(f'Минимальное число: {min_num}, максимальное число: {max_num}')
print(f'Сумма элементов массива без макс. и мин. элементов: {sum_num}')
