import sys
N = int(sys.stdin.readline().strip())
factors = list(map(int, sys.stdin.readline().strip().split()))
factors.sort()
if N == 1:
    print(factors[0] ** 2)
else:
    print(factors[-1] * factors[0])