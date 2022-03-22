#!/usr/bin/env python3

from typing import List

N, K = [int(e) for e in input().split()]
D: List[int] = []

remaining = set()
for i, e in enumerate(input().split()):
    remaining.add(i)
    D.append(int(e) - 1)

count = 0
while remaining:
    node_i = remaining.pop()
    linked = set()
    while True:
        linked.add(node_i)
        node_i = D[node_i]
        if node_i in linked:
            break
        remaining.remove(node_i)
        count += 1

k = K - count
print("YES" if k >= 0 and k % 2 == 0 else "NO", end="")
