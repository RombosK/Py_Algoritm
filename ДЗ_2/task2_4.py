# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

# n = int(input())
def parity_nums(n: int):
    cnt = 0
    for i in range(1, n+1):
        cnt += i
    right = n * (n + 1) // 2
    print(cnt)
    print(right)
    if cnt == right:
        return print(f'Равенство верное')


parity_nums(10)
# parity_nums(6)
# parity_nums(100)
# parity_nums(0)



