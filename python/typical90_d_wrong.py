import sys

H, W = sys.stdin.readline().split()

table = []
for row in range(int(H)):
    table.append([int(elem) for elem in sys.stdin.readline().split()])


for row in range(int(H)):
    for col in range(int(W)):
        total = sum(table[row])
        for row2 in range(int(H)):
            if row == row2:
                continue
            total += table[row2][col]
        print(total, end=" ")
    print()

