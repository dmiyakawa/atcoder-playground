#!/usr/bin/env python3

import sys

N = int(sys.stdin.readline())
s = set()

for i in range(N):
    s.add(int(sys.stdin.readline()))

print(len(s), end="")
