import sys
from collections import deque
T = int(sys.stdin.readline().strip())

def solution(orders, nums):
    original = True
    for order in orders:
        if order == "R":
            if original:
                original = False
            else:
                original = True
        else:
            if nums:
                if original:
                    nums.popleft()
                else:
                    nums.pop()
            else:
                return "error"
    if original:
        return nums
    else:
        nums.reverse()
        return nums


for i in range(T):
    orders = sys.stdin.readline().strip().replace("RR", "")
    # print(orders)
    N = int(sys.stdin.readline().strip())
    numbers = sys.stdin.readline().strip()
    if N == 0:
        num_list = []
    else:
        num_list = list(map(int, numbers[1:-1].split(",")))
    ret = solution(orders, deque(num_list))
    if ret == "error":
        print("error")
    else:
        if ret:
            print("[", end="")
            last = ret.pop()
            if ret:
                for r in ret:
                    print(r, end=",")
            print(last, end="")
            print("]")
        else:
            print([])


"""
1
D
1
[42]
"""