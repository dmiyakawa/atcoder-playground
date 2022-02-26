#!/usr/bin/env python

import sys


def main():
    lst = sys.stdin.read().split()
    n = 0
    for i in range(3):
        n = int(lst[n])
    print(n, end="")


if __name__ == "__main__":
    main()
