#!/usr/bin/env python3

import sys

N, A, B = [int(e) for e in sys.stdin.readline().split()]

total = 0
for i in range(1, N + 1):
    s = i % 10 + ((i // 10) % 10) + ((i // 100) % 10) + ((i // 1000) % 10) + ((i // 10000) % 10)
    if A <= s <= B:
        total += i

print(total, end="")
