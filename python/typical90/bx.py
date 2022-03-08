#!/usr/bin/env python3

import sys

N = int(sys.stdin.readline())

a_s = [int(e) for e in sys.stdin.readline().split()]
target = sum(a_s) / 10

head = 1
tail = 0
current_mass = a_s[0]

answer_exists = False
while True:
    if current_mass == target:
        answer_exists = True
        break
    elif current_mass < target:
        current_mass += a_s[head]
        head = (head + 1) % N
    else:
        current_mass -= a_s[tail]
        tail = (tail + 1) % N
        if tail == 0:
            break

if current_mass == target:
    answer_exists = True

print("Yes" if answer_exists else "No", end="")
