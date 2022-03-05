#!/usr/bin/env python3

import sys


def calc():
    A, B, C, X = [int(e) for e in sys.stdin.readline().split()]
    if X <= A:
        return 1.0
    elif X <= B:
        return C / (B - A)
    else:
        return 0.0


def main():
    print(calc(), end="")


if __name__ == "__main__":
    main()

