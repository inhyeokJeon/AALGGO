import sys
import math
N, K = list(map(int, sys.stdin.readline().strip().split()))

print(math.comb(N, K) % 10007)
