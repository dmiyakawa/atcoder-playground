#!/usr/bin/env python3

import sys

N = int(sys.stdin.readline())

names = set()

for i in range(1, N + 1):
    name = sys.stdin.readline().rstrip()
    if name not in names:
        names.add(name)
        print(i)

