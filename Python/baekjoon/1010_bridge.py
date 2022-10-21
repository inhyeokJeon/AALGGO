import sys
import math
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, K = list(map(int, sys.stdin.readline().strip().split()))
    print(math.comb(K, N))
