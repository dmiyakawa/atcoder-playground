#!/usr/bin/env python3

import sys

N, K = [int(e) for e in sys.stdin.readline().split()]
a_s = [int(e) for e in sys.stdin.readline().split()]
b_s = [int(e) for e in sys.stdin.readline().split()]

rem = K - sum(abs(a_s[i] - b_s[i]) for i in range(N))
ans = "Yes" if rem >= 0 and rem % 2 == 0 else "No"
print(ans, end="")
