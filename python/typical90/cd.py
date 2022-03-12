#!/usr/bin/env python3

import sys

DIV_VAL = 10 ** 9 + 7


def count_num_digits(n):
    num_digits = 0
    while n:
        num_digits += 1
        n //= 10
    return num_digits


def main():
    L, R = [int(e) for e in sys.stdin.readline().split()]
    num_digits_l = count_num_digits(L)
    num_digits_r = count_num_digits(R)
    ans = 0
    if num_digits_l == num_digits_r:
        ans = (num_digits_l * (R * (R + 1) // 2 - (L - 1) * L // 2)) % DIV_VAL
    else:
        for num_digits in range(num_digits_l, num_digits_r + 1):
            if num_digits == num_digits_l:
                tmp = 10 ** num_digits - 1
                ans += (num_digits * (tmp * (tmp + 1) // 2 - (L - 1) * L // 2)) % DIV_VAL
            elif num_digits == num_digits_r:
                tmp = 10 ** (num_digits - 1)
                ans += (num_digits * (R * (R + 1) // 2 - (tmp - 1) * tmp // 2)) % DIV_VAL
            else:
                left = 10 ** (num_digits - 1)
                right = 10 ** num_digits - 1
                ans += (num_digits * (right * (right + 1) // 2 - (left - 1) * left // 2)) % DIV_VAL

    print(ans % DIV_VAL)


if __name__ == "__main__":
    main()
