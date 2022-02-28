#!/usr/bin/env python3
#
# https://atcoder.jp/contests/abs/tasks/abc085_c
#

import sys


def main():
    lst = sys.stdin.readline().rstrip().split()
    n, y = int(lst[0]), int(lst[1])
    # n10000, n5000, n1000
    for n10000 in range(n, -1, -1):
        if n10000 * 10_000 + (n - n10000) * 1000 > y:
            continue
        elif n10000 * 10_000 + (n - n10000) * 5000 < y:
            break
        for n5000 in range(n - n10000, -1, -1):
            n1000 = n - n10000 - n5000
            total = n10000 * 10_000 + n5000 * 5_000 + n1000 * 1_000
            if total == y:
                print(n10000, n5000, n1000, end="")
                return
            elif total < y:
                break

    print(-1, -1, -1, end="")
    # print()


if __name__ == "__main__":
    main()
