# https://www.acmicpc.net/problem/2263
import sys
from collections import defaultdict, deque
sys.setrecursionlimit(1000000)

def main():
    n = int(sys.stdin.readline().strip())
    inorder = list(map(int, sys.stdin.readline().strip().split()))
    postorder = list(map(int, sys.stdin.readline().strip().split()))
    temp = [0] * (n + 1)
    for i in range(n):
        
        temp[inorder[i]] = i
    def solve(in_order_start, in_order_end, post_order_start, post_order_end):
        if in_order_start > in_order_end or post_order_start > post_order_end:
            return
        root_index = temp[postorder[post_order_end]]
        left = root_index - in_order_start # left 개수.
        right = in_order_end - root_index  # right 개수.
        # ret.append(inorder[root_index])
        print(postorder[post_order_end], end= " ")
        solve(in_order_start, in_order_start + left - 1, post_order_start, post_order_start + left - 1)
        solve(in_order_end - right + 1, in_order_end, post_order_end - right, post_order_end - 1)

    solve(0, n - 1, 0, n - 1)

if __name__ == "__main__":
    main()

"""
9
4 2 5 1 9 7 6 8 3
4 5 2 9 7 8 6 3 1
"""
# 1 2 4 5 3 6 7 9 8
