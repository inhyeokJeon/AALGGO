import sys
from collections import deque, defaultdict
import heapq
MAX = 100_000
def main():
    n, k = list(map(int, sys.stdin.readline().strip().split()))

    visited = [-1] * (MAX + 1)
    moved = [-1] * (MAX + 1)

    def bfs(i):
        q = deque()
        q.append(i)
        visited[i] = 0
        while q:
            r = q.popleft()
            for next in (r - 1, r + 1, r * 2):
                if 0 <= next <= MAX and visited[next] == -1:
                    q.append(next)
                    visited[next] = visited[r] + 1
                    moved[next] = r

    bfs(n)
    ret = visited[k]
    start = k
    result = [start]
    for _ in range(ret):
        start = moved[start]
        result.append(start)

    print(ret)
    print(*result[::-1])

if __name__ == "__main__":
    main()
