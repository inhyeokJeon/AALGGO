import sys
from collections import Counter
T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    if N == 0:
        print(0)
        continue
    clothes = Counter()
    for i in range(N):
        name, kind = sys.stdin.readline().strip().split()
        clothes[kind] += 1
    ret = 1
    for cloth in clothes:
        ret *= (clothes[cloth] + 1)
    print(ret - 1)
