import sys
import bisect

K, N = list(map(int, sys.stdin.readline().strip().split()))
cands = list(map(int, sys.stdin.readline().strip().split()))
answer = 0
def solve(num):
    count = 0
    for cand in cands:
        temp = cand - num
        if temp > 0:
            count += temp
    if count < N:
        return False
    return True

def solution():
    global answer
    left = 1
    right = max(cands)
    while left <= right:
        mid = (left + right) // 2
        if solve(mid):
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1

solution()
print(answer)