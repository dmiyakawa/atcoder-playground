#!/usr/bin/env python3
#
# https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/all/DPL_1_B
#

import sys
from typing import Tuple, List, Optional

# N個の品物、容量がW
N, W = [int(e) for e in sys.stdin.readline().split()]
items: List[Optional[Tuple[int, int]]] = [None]
for i in range(N):
    value, weight = [int(e) for e in sys.stdin.readline().split()]
    items.append((value, weight))

table = [[0] * (W + 1)]
for n in range(1, N + 1):
    lst = [0]
    table.append(lst)
    item = items[n]
    for w in range(1, W + 1):
        cand_1 = table[n - 1][w]
        cand_2 = table[n - 1][w - item[1]] + item[0] if w - item[1] >= 0 else 0
        lst.append(max(cand_1, cand_2))

print(table[N][W])
