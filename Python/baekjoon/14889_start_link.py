import sys
import itertools
N = int(sys.stdin.readline().strip())

tables = [None] * N
for _ in range(N):
    tables[_] = list(map(int,sys.stdin.readline().strip().split()))
result = float("inf")
for i in itertools.combinations(range(N), N // 2):
    start_score, link_score = 0, 0
    start = set(list(range(N))) - set(i)
    link = set(i)
    for i, j in itertools.permutations(start, 2):
        start_score += tables[i][j]
    for i, j in itertools.permutations(link, 2):
        link_score += tables[i][j]
    result = min(result, abs(start_score - link_score))
print(result)