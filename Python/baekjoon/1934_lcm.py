import sys
import math
N = int(sys.stdin.readline().strip())
for _ in range(N):
    n, m = list(map(int, sys.stdin.readline().strip().split()))

    print(math.lcm(n, m))

