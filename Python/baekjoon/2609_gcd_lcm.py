import sys
import math
N, M = list(map(int, sys.stdin.readline().strip().split()))

print(math.gcd(N, M))
print(math.lcm(N, M))

