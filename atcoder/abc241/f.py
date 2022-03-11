#!/usr/bin/env python
#
# TLE (and probably wrong)
# https://atcoder.jp/contests/abc241/submissions/29724641
# https://atcoder.jp/contests/abc241/submissions/29724767
#

import sys
from typing import Tuple, Set, Dict, List


def calc_moves(w, s_x, s_y, g_x, g_y, x_to_ys, y_to_xs) -> int:
    if (s_x, s_y) == (g_x, g_y):
        return 0
    reachables: Dict[Tuple[int, int], int] = {(g_x, g_y): 0}
    places_to_consider: List[Tuple[int, int]] = [(g_x, g_y)]
    while places_to_consider:
        c_x, c_y = places_to_consider.pop()
        num_moves = reachables[(c_x, c_y)]

        def consider_vertically(x, y):
            if (x, y) == (s_x, s_y) or x_to_ys.get(x, set()) & {y + 1, y - 1}:
                current_num_moves = reachables.get((x, y), 10000000000)
                if num_moves + 1 < current_num_moves:
                    reachables[(x, y)] = num_moves + 1
                    places_to_consider.append((x, y))

        def consider_horizontally(x, y):
            if (x, y) == (s_x, s_y) or y_to_xs.get(y, set()) & {x + 1, x - 1}:
                current_num_moves = reachables.get((x, y), 10000000000)
                if num_moves + 1 < current_num_moves:
                    reachables[(x, y)] = num_moves + 1
                    places_to_consider.append((x, y))

        if c_y in x_to_ys.get(c_x + 1, set()):
            for t_x in range(c_x):
                consider_vertically(t_x, c_y)
        if c_y in x_to_ys.get(c_x - 1, set()):
            for t_x in range(c_x + 1, w):
                consider_vertically(t_x, c_y)
        if c_x in y_to_xs.get(c_y + 1, set()):
            for t_y in range(c_y):
                consider_horizontally(c_x, t_y)
        if c_x in y_to_xs.get(c_y - 1, set()):
            for t_y in range(c_y + 1, w):
                consider_horizontally(c_x, t_y)
    return reachables.get((s_x, s_y), -1)


def main():
    (h, w, n) = [int(e) for e in sys.stdin.readline().split()]
    (s_x, s_y) = [int(e) - 1 for e in sys.stdin.readline().split()]
    (g_x, g_y) = [int(e) - 1 for e in sys.stdin.readline().split()]
    obstacles: Set[Tuple[int, int]] = set()
    x_to_ys: Dict[int, Set[int]] = {}
    y_to_xs: Dict[int, Set[int]] = {}
    for i in range(n):
        (o_x, o_y) = [int(e) - 1 for e in sys.stdin.readline().split()]
        obstacles.add((o_x, o_y))
        x_to_ys.setdefault(o_x, set()).add(o_y)
        y_to_xs.setdefault(o_y, set()).add(o_x)
    print(calc_moves(w, s_x, s_y, g_x, g_y, x_to_ys, y_to_xs), end="")


if __name__ == "__main__":
    main()
