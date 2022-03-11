# Одна задача на структуру данных "Непересекающиеся множества", рассмотренную на уроке.
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [x for x in range(n)]

        def union(a, b):
            parent[find(a)] = find(b)

        def find(a):
            if a != parent[a]:
                parent[a] = find(parent[a])
            return parent[a]

        for a, b in connections:
            union(a, b)

        elem = len(connections)
        if n - 1 > elem:
            return -1

        count = 0
        for a in range(n):
            if a == find(a):
                count += 1
        return count - 1
