#!/usr/bin/env python3
#
# https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_A
#

import sys

# M種類のコインを使ってN円支払う
N, M = [int(e) for e in sys.stdin.readline().split()]

NO_ANSWER = N + 1
c_s = [int(e) for e in sys.stdin.readline().split()]

min_coins = [[0] + [NO_ANSWER] * N]
for m in range(1, M + 1):
    lst = [0]
    min_coins.append(lst)
    coin = c_s[m - 1]
    for n in range(1, N + 1):
        cand_1 = NO_ANSWER
        if n - coin >= 0 and lst[n - coin] is not None:
            cand_1 = lst[n - coin] + 1
        cand_2 = NO_ANSWER
        if m > 0:
            cand_2 = min_coins[m - 1][n]
        min_coins[m].append(min(cand_1, cand_2))

# import pprint
# pprint.pprint(min_coins, width=300)
print(min_coins[M][N])
