#!/usr/bin/env python3

import sys

N = int(sys.stdin.readline())
a_s = sorted([int(e) for e in sys.stdin.readline().split()])
Q = int(sys.stdin.readline())


def bin_search(q):
    min_j, max_j = 0, N
    while max_j - min_j > 3:
        mid_j = (min_j + max_j) // 2
        score = a_s[mid_j] - q
        # print(f"# {mid_j=}, {a_s[mid_j]=}, {q=}, {score=}")

        if score == 0:
            return 0
        elif score > 0:  # mid_jが高すぎ
            max_j = mid_j + 1
        else:
            min_j = mid_j
    return min(abs(a_s[i] - q) for i in range(min_j, max_j))


def main():
    for i in range(Q):
        print(bin_search(int(sys.stdin.readline())))


if __name__ == "__main__":
    main()



