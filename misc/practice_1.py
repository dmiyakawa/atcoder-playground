import sys

lst = sys.stdin.read().split()
print("{} {}".format(int(lst[0]) + int(lst[1]) + int(lst[2]), lst[3]))
