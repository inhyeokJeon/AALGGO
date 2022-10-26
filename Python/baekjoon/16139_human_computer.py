import sys
from collections import defaultdict
S = sys.stdin.readline().strip()
Q = int(sys.stdin.readline().strip())

temp = defaultdict(list)

for i in "abcedfghijklmnopqrstuvwxyz":
    temp[i] = [0] * (len(S) + 1)

for idx, s in enumerate(S):
    for key in temp:
        if s == key:
            temp[key][idx + 1] = temp[key][idx] + 1
        else:
            temp[key][idx + 1] = temp[key][idx]

for i in range(Q):
    alpha, start, end = sys.stdin.readline().strip().split()
    start, end = int(start), int(end)
    print(temp[alpha][end + 1] - temp[alpha][start])
