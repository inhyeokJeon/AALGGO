import sys
import bisect
N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
numbers.sort()
M = int(sys.stdin.readline().strip())
cands = list(map(int, sys.stdin.readline().strip().split()))

for cand in cands:
    index = bisect.bisect_left(numbers, cand)
    if index >= len(numbers) or numbers[index] != cand:
        print(0)
    else:
        print(1)
