#!/usr/bin/env python3

import sys


def trans(n_reversed):
    num = 0
    for i, d8 in enumerate(n_reversed):
        num += int(d8) * (8 ** i)
    new_n_reversed = []
    while num:
        digit9 = num % 9
        if digit9 == 8:
            digit9 = 5
        new_n_reversed.append(str(digit9))
        num = num // 9
    if not new_n_reversed:
        new_n_reversed = ["0"]
    return new_n_reversed


def main():
    lst = sys.stdin.readline().split()
    n_reversed, K = reversed(lst[0]), int(lst[1])

    for _ in range(K):
        n_reversed = trans(n_reversed)
    print("".join(str(e) for e in reversed(n_reversed)))


if __name__ == "__main__":
    main()







