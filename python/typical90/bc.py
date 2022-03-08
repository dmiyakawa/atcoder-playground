#!/usr/bin/env python3

import itertools
import sys

E, P, Q = [int(e) for e in sys.stdin.readline().split()]
a_s = [int(e) % P for e in sys.stdin.readline().split()]

count = 0
for comb in itertools.combinations(a_s, 5):
    if (((((((comb[0] * comb[1]) % P) * comb[2]) % P) * comb[3]) % P) * comb[4]) % P == Q:
        count += 1

print(count, end="")
