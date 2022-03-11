#!/usr/bin/env python3
#
# フィボナッチ
#

import sys


def search_fib_index(fib, k):
    i = 0
    while fib[i] < k:
        i += 1
    return i


def main():
    S = sys.stdin.readline().strip()
    fib = [1, 1]
    for i in range(2, 102):
        fib.append(fib[i - 1] + fib[i - 2])

    Q = int(sys.stdin.readline())
    for i in range(Q):
        t, k = [int(e) for e in sys.stdin.readline().split()]
        fib_i = search_fib_index(fib, k)
        print(t, k, fib_i)


if __name__ == "__main__":
    main()
