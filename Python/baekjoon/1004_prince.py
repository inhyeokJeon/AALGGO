import sys
import math


def solve():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        result = 0
        s_x, s_y, d_x, d_y = list(map(int, sys.stdin.readline().strip().split()))
        N = int(sys.stdin.readline().strip())
        planets = []
        for _ in range(N):
            # x, y, r
            planets.append(list(map(int, sys.stdin.readline().strip().split())))

        for x, y, r in planets:
            dist_s = math.sqrt(math.pow(abs(x - s_x), 2) + math.pow(abs(y - s_y), 2))
            dist_d = math.sqrt(math.pow(abs(x - d_x), 2) + math.pow(abs(y - d_y), 2))
            if dist_d < r and dist_s < r:
                continue
            if dist_d < r:
                result += 1
            if dist_s < r:
                result += 1
        print(result)
solve()