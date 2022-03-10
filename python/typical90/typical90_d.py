import sys

H, W = [int(e) for e in sys.stdin.readline().split()]

table = []
totals_per_row = []
totals_per_col = [0] * W

for row_index in range(H):
    row = [int(elem) for elem in sys.stdin.readline().split()]
    table.append(row)
    totals_per_row.append(sum(row))
    for col_index in range(W):
        totals_per_col[col_index] += row[col_index]


for row_index in range(int(H)):
    answer_row = []
    for col_index in range(int(W)):
        answer_row.append(totals_per_row[row_index] + totals_per_col[col_index] - table[row_index][col_index])
    print(" ".join(str(s) for s in answer_row))
