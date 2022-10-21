import sys
import itertools

N, M = list(map(int,sys.stdin.readline().strip().split()))

for perm in itertools.product(range(1, N + 1), repeat = M):
    print(*perm)
