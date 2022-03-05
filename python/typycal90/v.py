#!/usr/bin/env python3
#
# https://atcoder.jp/contests/typical90/tasks/typical90_v
#

import sys


def gcd(a, b):
    while True:
        if a < b:
            a, b = b, a
        r = a % b
        if r == 0:
            return b
        a = b
        b = r


A, B, C = [int(e) for e in sys.stdin.readline().split()]

n = gcd(gcd(A, B), C)
print("{:d}".format((A // n - 1) + (B // n - 1) + (C // n - 1)), end="")

