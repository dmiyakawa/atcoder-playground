#!/usr/bin/env python3

import sys


def main():
    S = sys.stdin.readline().rstrip()
    print(''.join(sorted(S)), end="")


if __name__ == "__main__":
    main()
