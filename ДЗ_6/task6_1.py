# Параллельная обработка
# По данным n процессорам и m задач определите, для каждой из задач,каким процессором она будет обработана.
# Вход. Число процессоров n и последовательность чисел t0, . . . , tm−1, где ti — время, необходимое на обработку i-й задачи.
# Выход. Для каждой задачи определите, какой процессор и в какое время начнёт её обрабатывать, предполагая, что
# каждая задача поступает на обработку первому освободившемуся процессору.
import queue
import sys

processors = sys.stdin.readline().split(' ')
tasks = sys.stdin.readline().split(' ')
proc = int(processors[0])
quantity = int(processors[1])
tree = queue.PriorityQueue()

for el in range(proc):
    tree.put([0, proc, el])
for nums in tasks:
    nums = int(nums)
    up = tree.get()
    if nums < 1:
        print(up[2], up[0])
        tree.put(up)
        continue
    else:
        print(up[2], up[0])
        up[0] += nums
        tree.put(up)


# from heapq import heapreplace
# process = [(0, el) for el in range(int(input().split()[0]))]
# for num in map(int, input().split()):
#     print(*reversed(heapreplace(process, (process[0][0] + num, process[0][1]))))