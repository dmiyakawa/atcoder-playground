#!/usr/bin/env python3
#
# https://twitter.com/e869120/status/1412179495868534784/photo/3
#

import sys

N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
assert len(s) == N

total_combs = 0

last_o_pos = -1
last_x_pos = -1

for i, ch in enumerate(s):
    if ch == "o":
        last_o_pos = i
    else:
        last_x_pos = i
    if last_o_pos >= 0 and last_x_pos >= 0:
        total_combs += min(last_o_pos, last_x_pos) + 1

print(total_combs, end="")
