#!/usr/bin/env python3

import sys


def main():
    n = int(sys.stdin.readline())
    s = list(sys.stdin.readline().rstrip())
    ans = []
    i = 0
    while i < len(s):
        # print("".join(ans), s[i:])
        if s[i] == "B" and i < n - 1:
            if s[i + 1] == "A":
                ans.append("A")
                s[i + 1] = "B"
                i += 1
            elif s[i + 1] == "B":
                ans.append("A")
                i += 2
            else:
                ans.extend([s[i], s[i + 1]])
                i += 2
        else:
            ans.append(s[i])
            i += 1
    print("".join(ans), end="")


if __name__ == "__main__":
    main()
