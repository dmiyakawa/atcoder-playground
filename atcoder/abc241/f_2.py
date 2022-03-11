#!/usr/bin/env python
#
# https://atcoder.jp/contests/abc241/tasks/abc241_f
#
# AC with Python3
# https://atcoder.jp/contests/abc241/submissions/29732139
#
# AC with PyPy3
# https://atcoder.jp/contests/abc241/submissions/29732220
#

import sys
from typing import Tuple, Set, Dict, List

MAX_STEPS = 10**9


def calc() -> int:
    (x_max, y_max, n) = [int(e) for e in sys.stdin.readline().split()]
    (s_x, s_y) = [int(e) - 1 for e in sys.stdin.readline().split()]
    (g_x, g_y) = [int(e) - 1 for e in sys.stdin.readline().split()]

    # obstacles: Set[Tuple[int, int]] = set()
    obstacle_x_to_ys: Dict[int, Set[int]] = {}
    obstacle_y_to_xs: Dict[int, Set[int]] = {}

    reachable_x_to_ys: Dict[int, Set[int]] = {}
    reachable_y_to_xs: Dict[int, Set[int]] = {}

    for i in range(n):
        elem = sys.stdin.readline().split()
        (o_x, o_y) = (int(elem[0]) - 1, int(elem[1]) - 1)
        # obstacles.add((o_x, o_y))
        obstacle_x_to_ys.setdefault(o_x, set()).add(o_y)
        obstacle_y_to_xs.setdefault(o_y, set()).add(o_x)

        if o_x + 1 < x_max:
            reachable_x_to_ys.setdefault(o_x + 1, set()).add(o_y)
            reachable_y_to_xs.setdefault(o_y, set()).add(o_x + 1)
        if o_x - 1 >= 0:
            reachable_x_to_ys.setdefault(o_x - 1, set()).add(o_y)
            reachable_y_to_xs.setdefault(o_y, set()).add(o_x - 1)
        if o_y + 1 < y_max:
            reachable_x_to_ys.setdefault(o_x, set()).add(o_y + 1)
            reachable_y_to_xs.setdefault(o_y + 1, set()).add(o_x)
        if o_y - 1 >= 0:
            reachable_x_to_ys.setdefault(o_x, set()).add(o_y - 1)
            reachable_y_to_xs.setdefault(o_y - 1, set()).add(o_x)

    reachable_x_to_ys.setdefault(s_x, set()).add(s_y)
    reachable_y_to_xs.setdefault(s_y, set()).add(s_x)

    visited: Set[Tuple[int, int]] = set()
    places_to_consider: List[Tuple[int, int, int]] = [(s_x, s_y, 0)]
    # BFS
    while places_to_consider:
        cur_x, cur_y, cur_num_steps = places_to_consider.pop(0)
        if (cur_x, cur_y) in visited:
            continue
        visited.add((cur_x, cur_y))
        # print(f"cur: ({cur_x}, {cur_y}, {cur_num_steps}), {places_to_consider}")
        next_num_steps = cur_num_steps + 1
        for cand_y in reachable_x_to_ys[cur_x]:
            if (cur_x, cand_y) in visited:
                continue

            o_tmp = obstacle_x_to_ys.get(cur_x)
            obstacle_behind = o_tmp and (cand_y + 1 in o_tmp or cand_y - 1 in o_tmp)
            if not obstacle_behind:
                continue

            obstacle_exists = False
            for obs_y in obstacle_x_to_ys.setdefault(cur_x, set()):
                if (cur_y < obs_y < cand_y) or (cand_y < obs_y < cur_y):
                    obstacle_exists = True
                    break
            if obstacle_exists:
                continue

            # print(f"  ({cur_x}, {cand_y}) -> {obstacle_behind}")
            if (cur_x, cand_y) == (g_x, g_y):
                return next_num_steps
            places_to_consider.append((cur_x, cand_y, next_num_steps))

        for cand_x in reachable_y_to_xs[cur_y]:
            if (cand_x, cur_y) in visited:
                continue

            o_tmp = obstacle_y_to_xs.get(cur_y)
            obstacle_behind = o_tmp and (cand_x + 1 in o_tmp or cand_x - 1 in o_tmp)
            if not obstacle_behind:
                continue

            obstacle_exists = False
            for obs_x in obstacle_y_to_xs.setdefault(cur_y, set()):
                if (cur_x < obs_x < cand_x) or (cand_x < obs_x < cur_x):
                    obstacle_exists = True
                    break
            if obstacle_exists:
                continue

            # print(f"  ({cand_x}, {cur_y}) -> {obstacle_behind}")
            if (cand_x, cur_y) == (g_x, g_y):
                return next_num_steps
            places_to_consider.append((cand_x, cur_y, next_num_steps))

    return -1


if __name__ == "__main__":
    print(calc(), end="")

