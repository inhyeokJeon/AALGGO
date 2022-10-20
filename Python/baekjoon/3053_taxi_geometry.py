import math
import sys

N = int(sys.stdin.readline().strip())
first = round(math.pi * math.pow(N, 2), 6)
second = math.pow(2 * N, 2) // 2

print(f"{first:.6f}")
print(f"{second:.6f}")