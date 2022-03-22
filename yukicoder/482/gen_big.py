#!/usr/bin/env python3

import random

N = 200_000
K = 10**12
lst = [str(i) for i in range(1, N + 1)]
random.shuffle(lst)
print(N, K)
print(" ".join(lst))
