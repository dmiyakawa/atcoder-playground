#!/usr/bin/env python3

import sys

H, W = [int(e) for e in sys.stdin.readline().split()]
if W == 1:
    ans = H
elif H == 1:
    ans = W
else:
    ans = (H // 2 + H % 2) * (W // 2 + W % 2)
print(ans, end="")
