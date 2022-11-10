import sys
from collections import deque

MAX = 200_000
def main():
    n, k = list(map(int, sys.stdin.readline().strip().split()))

    visited = [0] * (MAX + 1)


    def bfs(i):
        q = deque()
        q.append((i, 0))
        ret = float("inf")
        while q:
            r, count = q.popleft()
            if visited[r]:
                continue
            visited[r] = count
            if r == k:
                ret = min(ret, count)
                continue
            if r > k:
                ret = min(ret, count + r - k)
                continue
            q.append((r + 1, count + 1))
            if not r - 1 < 0:
                q.append((r - 1, count + 1))
            q.append((2 * r, count + 1))

        return ret

    print(bfs(n))


if __name__ == "__main__":
    main()
