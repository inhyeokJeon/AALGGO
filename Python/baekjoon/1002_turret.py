import sys
import math
N = int(sys.stdin.readline().strip())

for _ in range(N):
    c_x, c_y, c_r, b_x, b_y, b_r = list(map(int, sys.stdin.readline().strip().split()))
    dist = math.sqrt(math.pow(abs(c_x - b_x), 2) + math.pow(abs(c_y - b_y), 2))
    if dist == 0: # case 4 5
        if c_r == b_r:
            print(-1)
        else:
            print(0)
    else:
        if c_r > b_r:
            # 포함
            if c_r > dist + b_r:
                print(0)
            elif c_r == dist + b_r: # 겹침
                print(1)
            else: # 불포함
                if dist == b_r + c_r:
                    print(1)
                elif dist < b_r + c_r:
                    print(2)
                else:
                    print(0)
        elif b_r > c_r:
            # 포함
            if b_r > dist + c_r:
                print(0)
            elif b_r == dist + c_r:
                print(1)
            else:
                if dist == b_r + c_r:
                    print(1)
                elif dist < b_r + c_r:
                    print(2)
                else:
                    print(0)
            # print(b_r, "dist?", dist + c_r)
        else: # 반지름이 같다면
            if dist == b_r + c_r:
                print(1)
            elif dist < b_r + c_r:
                print(2)
            else:
                print(0)

    # print("dist:", dist)
