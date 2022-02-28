#!/usr/bin/env python3
#
# https://atcoder.jp/contests/abs/tasks/abc085_c
#

import sys


def main():
    # 1 <= N <= 100000
    N = int(sys.stdin.readline())
    subtotals = [[], []]
    for i in range(N):
        tmp = sys.stdin.readline().split()
        c, p = int(tmp[0]) - 1, int(tmp[1])
        subtotals[c].append((subtotals[c][i - 1] if i > 0 else 0) + p)
        subtotals[(c + 1) % 2].append(subtotals[(c + 1) % 2][i - 1] if i > 0 else 0)

    Q = int(sys.stdin.readline())
    for i in range(Q):
        tmp = sys.stdin.readline().split()
        left, right = int(tmp[0]) - 1, int(tmp[1]) - 1
        a = subtotals[0][right] - (subtotals[0][left - 1] if left > 0 else 0)
        b = subtotals[1][right] - (subtotals[1][left - 1] if left > 0 else 0)
        print(f"{a} {b}")


if __name__ == "__main__":
    main()
