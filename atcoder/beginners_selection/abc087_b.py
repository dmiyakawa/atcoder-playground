#!/usr/bin/env python3

import sys

A, B, C, X = [int(e) for e in sys.stdin.readlines()]

count = 0
for num_a in range(A + 1):
    rem_a = X - 500 * num_a
    for num_b in range(B + 1):
        rem_b = rem_a - 100 * num_b
        if rem_b < 0:
            break
        elif rem_b % 50 == 0 and rem_b // 50 <= C:
            count += 1


print(count, end="")

