# Обработка сетевых пакетов.Реализовать обработчик сетевых пакетов.
from collections import deque

size, n = map(int, input().split())
result = deque()
for i in range(n):
    arrival, duration = map(int, input().split())

    while result and result[0] <= arrival:
        result.popleft()

    if len(result) < size:
        if result:
            arrival = max(arrival, result[-1])
        print(arrival)
        result.append(arrival + duration)
    else:
        print(-1)

# Другого решения не придумалось

