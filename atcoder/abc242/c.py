#!/usr/bin/env python3

import sys


def main():
    N = int(sys.stdin.readline())
    cache = []
    for i in range(N):
        d = {}
        cache.append(d)
        if i == 0:
            for j in range(1, 10):
                d[j] = 1
        else:
            for j in range(1, 10):
                if j == 1:
                    d[j] = (cache[i - 1][1] + cache[i - 1][2]) % 998244353
                elif j == 9:
                    d[j] = (cache[i - 1][8] + cache[i - 1][9]) % 998244353
                else:
                    d[j] = (cache[i - 1][j - 1] + cache[i - 1][j] + cache[i - 1][j + 1]) % 998244353
    print(sum(cache[N-1].values()) % 998244353, end="")


if __name__ == "__main__":
    main()
