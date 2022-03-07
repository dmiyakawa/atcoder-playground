#!/usr/bin/env python3

import sys

sys.stdin.readline()

total_alice = 0
total_bob = 0
for i, e in enumerate(sorted([int(e) for e in sys.stdin.readline().split()], reverse=True)):
    a = int(e)
    if i % 2 == 0:
        total_alice += a
    else:
        total_bob += a

print(total_alice - total_bob, end="")


