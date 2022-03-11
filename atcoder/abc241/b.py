#!/usr/bin/env python

import sys


def main():
    (n, m) = [int(elem) for elem in sys.stdin.readline().split()]
    a_s = {}
    for elem in sys.stdin.readline().split():
        val = int(elem)
        a_s[val] = a_s.get(val, 0) + 1
    for elem in sys.stdin.readline().split():
        val = int(elem)
        remaining = a_s.get(val, 0)
        if remaining == 0:
            print("No", end="")
            return
        a_s[val] = remaining - 1
    print("Yes", end="")


if __name__ == "__main__":
    main()
