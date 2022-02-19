# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random


arr = [random.randint(0, 20) for i in range(10)]
print(arr)
min_idx1 = 0
min_idx2 = 1

for i in arr:
    if arr[min_idx1] > i:
        min_idx2 = min_idx1
        min_idx1 = arr.index(i)
    elif arr[min_idx2] > i:
        min_idx2 = arr.index(i)


print(f'Два наименьших элемента: {arr[min_idx1]} и {arr[min_idx2]}')
