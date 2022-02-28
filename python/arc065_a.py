#!/usr/bin/env python3
#
# https://atcoder.jp/contests/abs/tasks/arc065_a
#

import sys


def check() -> bool:
    s = sys.stdin.readline().rstrip()
    i = 0
    d = {
        "erasedre": 5,
        "eraseera": 5,
        "dreamdre": 5,
        "dreamera": 5,
        "eraserdr": 6,
        "eraserer": 6,
        "dreamerd": 7,
        "dreamere": 7,
    }

    while i < len(s):
        # print(s[i:], file=sys.stderr)
        if s[i:] in {"erase", "dream", "eraser", "dreamer"}:
            i += len(s[i:])
            continue
        steps = d.get(s[i:i+8])
        if steps:
            i += steps
        else:
            return False
    return True


if __name__ == "__main__":
    print("YES" if check() else "NO", end="")
