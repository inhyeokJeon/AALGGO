# https://www.acmicpc.net/problem/9019
import sys
from collections import deque


def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        A, B = list(map(int, sys.stdin.readline().strip().split()))
        visited = [False] * 10000

        def bfs(start):
            visited[start] = True
            dq = deque()
            dq.append((start, ""))
            while dq:
                node, order = dq.popleft()
                if node == B:
                    print(order)
                    return
                D_num = (2 * node) % 10000
                S_num = node - 1 if node != 0 else 9999
                L_num = 10 * (node % 1000) + node // 1000
                R_num = 1000 * (node % 10) + node // 10
                if not visited[D_num]:
                    dq.append((D_num, order + "D"))
                    visited[D_num] = True
                if not visited[S_num]:
                    dq.append((S_num, order + "S"))
                    visited[S_num] = True
                if not visited[L_num]:
                    dq.append((L_num, order + "L"))
                    visited[L_num] = True
                if not visited[R_num]:
                    dq.append((R_num, order + "R"))
                    visited[R_num] = True
        bfs(A)
if __name__ == "__main__":
    main()

