import sys

def solve():
    x, y, w, h = list(map(int, sys.stdin.readline().strip().split()))
    return min(w-x, x, h-y, y)

print(solve())