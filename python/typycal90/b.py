#!/usr/bin/env python3

import sys
from typing import List, Dict


def main(N):
    if N % 2 == 1:
        return
    num_parens = N // 2
    combs: Dict[int, List[List[int]]] = {}
    cache: Dict[int, List[str]] = {}
    in_stack = 0
    used = 0
    for n in range(1, num_parens + 1):
        for i in range(n, 0, -1):
            if i == n:
                combs[n] = [[i]]
            else:
                for comb in combs[i]
                    combs[n].append(combs[i] + combs[n - i])
            print(n, i, n - i)
    for i in range(1, num_parens+1):
        print(i, combs[i])


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    main(N)
