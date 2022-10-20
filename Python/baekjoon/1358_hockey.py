import sys
import math


def solve():
    W, H, X, Y, P = list(map(int, sys.stdin.readline().strip().split()))

    people = []
    for _ in range(P):
        people.append(list(map(int, sys.stdin.readline().strip().split())))
    result = 0
    r = H // 2
    for p_x, p_y in people:
        # 사각형 안에 있을 경우
        dist_l = math.sqrt(math.pow(abs(X - p_x), 2) + math.pow(abs(Y + r - p_y), 2))
        dist_r = math.sqrt(math.pow(abs(X + W - p_x), 2) + math.pow(abs(Y + r - p_y), 2))
        if X <= p_x <= X + W and Y <= p_y <= Y + H:
            result += 1
        elif dist_l <= r:
            result += 1
        elif dist_r <= r:
            result += 1
    print(result)
solve()