import sys
from collections import Counter
def solve():
    y_counter = Counter()
    x_counter = Counter()
    for _ in range(3):
        y, x = list(map(int, sys.stdin.readline().strip().split()))
        y_counter[y] += 1
        x_counter[x] += 1
    ans_y, ans_x = 0, 0
    for c in y_counter:
        if y_counter[c] == 1:
            ans_y = c
    for r in x_counter:
        if x_counter[r] == 1:
            ans_x = r

    print(ans_y, ans_x)

solve()