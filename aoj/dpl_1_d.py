#!/usr/bin/env python3

import bisect


def main():
    lis = []
    for elem in [int(input()) for _ in range(int(input()))]:
        if len(lis) == 0 or lis[-1] < elem:
            lis.append(elem)
        else:
            lis[bisect.bisect_left(lis, elem)] = elem
    print(len(lis))


if __name__ == "__main__":
    main()
