import sys
import itertools

N, M = list(map(int,sys.stdin.readline().strip().split()))

for perm in itertools.combinations(range(1, N + 1), M):
    print(*perm)
