#!/usr/bin/env python3

import sys


def main():
    # N問の試験、K分
    N, K = [int(e) for e in sys.stdin.readline().split()]
    lst = []
    for i in range(N):
        a, b = [int(e) for e in sys.stdin.readline().split()]
        lst.append(b)
        lst.append(a - b)
    lst.sort(reverse=True)
    total = sum(lst[:K])
    print(total, end="")


if __name__ == "__main__":
    main()

