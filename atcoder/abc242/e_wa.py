#!/usr/bin/env python3

import sys


def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        total = 0
        N = int(sys.stdin.readline())
        S = sys.stdin.readline().rstrip()
        len_s = len(S)
        mid = len_s // 2 + len_s % 2
        for j, ch in enumerate(S[:mid]):
            # 回文の中央までで確実に辞書順の前になる文字列の数
            total = (total + (ord(ch) - ord("A")) * (26 ** (mid - j - 1))) % 998244353

        p_is_included = True
        for j in range(len_s // 2):
            left = len_s // 2 - 1 - j
            right = len_s // 2 + len_s % 2 + j
            # print(len(S), left, right, S[left], S[right])
            if S[left] > S[right]:
                p_is_included = False
                break
            elif S[left] < S[right]:
                break
        if p_is_included:
            total += 1
        print(total)


if __name__ == "__main__":
    main()
