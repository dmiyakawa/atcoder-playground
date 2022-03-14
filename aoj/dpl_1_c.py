#!/usr/bin/env python3
from typing import Dict


def main():
    N, W = [int(e) for e in input().split()]
    value_and_weight = []
    for _ in range(N):
        v, w = [int(e) for e in input().split()]
        value_and_weight.append((v, w))

    # weight -> value
    dp: Dict[int, int] = {0: 0}
    for w in range(1, W + 1):
        max_value = None
        for v1, w1 in value_and_weight:
            if w - w1 in dp:
                max_value = max(max_value, dp[w - w1] + v1) if max_value is not None else dp[w - w1] + v1
        if max_value is not None:
            dp[w] = max_value
    print(max(dp.values()))


if __name__ == "__main__":
    main()
