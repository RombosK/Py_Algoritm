# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
arr = [random.randint(0, 50) for i in range(10)]
print(f'Первоначальный массив: {arr}')
max = arr[0]
min = arr[0]
for i in arr:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = arr.index(min)
max_index = arr.index(max)
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
print(f'Массив после изменения: {arr}, индексы элементов: {min_index} и {max_index}')
