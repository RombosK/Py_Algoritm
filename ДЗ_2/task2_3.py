# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.


def sum_dig(n: int):
    first = 1
    summa = 0
    for i in range(n):
        summa += first
        first /= -2
    return summa


print(sum_dig(4))
print(sum_dig(2))
print(sum_dig(11))
