#!/usr/bin/env python3
#
# https://twitter.com/e869120/status/1412179495868534784/photo/2
#

import sys

N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
assert len(s) == N

total_comb = N * (N + 1) // 2

combs_to_be_excluded = 0

current_ch = None
current_count = 0

for ch in s:
    if current_ch is None:
        current_ch = ch
        current_count = 1
    elif current_ch == ch:
        current_count += 1
    else:
        current_ch = ch
        combs_to_be_excluded += current_count * (current_count + 1) // 2
        current_count = 1

combs_to_be_excluded += current_count * (current_count + 1) // 2

ans = total_comb - combs_to_be_excluded

print(ans, end="")
