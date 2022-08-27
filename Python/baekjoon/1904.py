import sys


def solve():
    n = int(sys.stdin.readline().strip())
    first = 0
    second = 1
    if n <= 3:
        return n
    for _ in range(n):
        ret = (second + first) % 15746
        first = second
        second = ret
    return ret


print(solve())
