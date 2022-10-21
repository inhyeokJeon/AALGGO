import sys
import math
N = int(sys.stdin.readline().strip())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline().strip()))

numbers.sort()
cands = []
ret = []
for i in range(1, N):
    cands.append(numbers[i] - numbers[i-1])

prev = cands[0]
for i in range(1, len(cands)):
    prev = math.gcd(prev, cands[i])

for i in range(2, prev + 1):
    if prev % i == 0:
        ret.append(i)

print(*ret)