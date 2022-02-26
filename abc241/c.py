#!/usr/bin/env python
#
# WA, TLE
#

import sys


def check(n, table):
    for row_index in range(n):
        for col_index in range(n):
            do_search_right = col_index + 5 < n
            do_search_left = col_index >= 5
            do_search_down = row_index + 5 < n
            if do_search_right and sum(table[row_index][col_index:col_index + 6]) >= 4:
                return True
            if do_search_down:
                count_v = 0
                count_d1 = 0
                count_d2 = 0
                for i in range(6):
                    count_v += table[row_index + i][col_index]
                    if do_search_right:
                        count_d1 += table[row_index + i][col_index + i]
                    if do_search_left:
                        count_d2 += table[row_index + i][col_index - i]
                if count_v >= 4 or count_d1 >= 4 or count_d2 >= 4:
                    return True
    return False


def main():
    n = int(sys.stdin.readline())
    table = []
    for i in range(n):
        table.append([1 if ch == "#" else 0 for ch in sys.stdin.readline().rstrip()])
    print("Yes" if check(n, table) else "No", end="")


if __name__ == "__main__":
    main()
