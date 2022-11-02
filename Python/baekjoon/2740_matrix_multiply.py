import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))
A = [None] * N
B = [None] * M
for i in range(N):
    A[i] = list(map(int, sys.stdin.readline().strip().split()))

M, K = list(map(int, sys.stdin.readline().strip().split()))
for i in range(M):
    B[i] = list(map(int, sys.stdin.readline().strip().split()))

def multi(f, s):
    ret = 0
    for i in range(len(f)):
        ret += (f[i] * s[i])
    return ret

def solve():
    changed = list(map(list, zip(*B)))
    result = []
    for i in range(N):
        temp = []
        for j in range(K):
            temp.append(multi(A[i], changed[j]))
        result.append(temp)
    for r in result:
        print(*r)

solve()