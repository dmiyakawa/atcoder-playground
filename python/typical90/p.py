#!/usr/bin/env python3
#
# TLE with pure Python
# AC with PyPy3
#

import sys


def search(n, a, b, c):
    current_min = 10000
    c_n = min(n // c, 9999)
    for c_i in range(c_n, -1, -1):
        b_n = n - c * c_i
        if b_n < 0:
            continue
        if c_i > current_min:
            continue
        for b_i in range(0, b_n + 1):
            if b_i + c_i > current_min:
                break
            a_n = n - c * c_i - b * b_i
            if a_n < 0:
                break
            if a_n % a != 0:
                continue
            a_i = a_n // a
            # print(f"# {n=}, {current_min=}, {a}*{a_i} + {b}*{b_i} + {c}*{c_i} = {a_i * a + b_i * b + c_i * c}")
            if c_i + b_i + a_i > current_min:
                continue

            current_min = min(a_i + b_i + c_i, current_min)
    return current_min


def main():
    N = int(sys.stdin.readline())
    A, B, C = sorted([int(e) for e in sys.stdin.readline().split()])
    print(search(N, A, B, C), end="")


if __name__ == "__main__":
    main()
