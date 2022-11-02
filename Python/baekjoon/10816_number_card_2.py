import sys
import bisect
N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
numbers.sort()
M = int(sys.stdin.readline().strip())
cands = list(map(int, sys.stdin.readline().strip().split()))

def solve(num):
    left = bisect.bisect_left(numbers, num)
    right = bisect.bisect_right(numbers, num)
    return right - left
for cand in cands:
    print(solve(cand), end=" ")
