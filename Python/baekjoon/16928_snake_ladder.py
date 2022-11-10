import sys
from collections import deque, defaultdict


def main():
    # 앞 뒤 북 동 남 서  y x h
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    ladders = defaultdict(int)
    snakes = defaultdict(int)

    visited = [False] * 101
    for i in range(n):
        start, end = list(map(int, sys.stdin.readline().strip().split()))
        # start, end = start - 1, end - 1
        ladders[start] = end

    for i in range(m):
        start, end = list(map(int, sys.stdin.readline().strip().split()))
        # start, end = start - 1, end - 1
        snakes[start] = end

    def out_of_range(x):
        return x <= 0 or x > 100

    def bfs(start):
        q = deque()
        q.append((start, 0))
        visited[start] = True
        count = 0
        while q:
            node, count = q.popleft()
            if node == 100:
                break
            for d in range(1, 7):
                next_node = node + d
                if out_of_range(next_node) or visited[next_node]:
                    continue
                visited[next_node] = True
                if ladders[next_node]:
                    if not visited[ladders[next_node]]:
                        q.append((ladders[next_node], count + 1))
                        visited[ladders[next_node]]
                    continue
                elif snakes[next_node]:
                    if not visited[snakes[next_node]]:
                        q.append((snakes[next_node], count + 1))
                        visited[snakes[next_node]]
                    continue
                else:
                    q.append((next_node, count + 1))

        return count
    print(bfs(1))

if __name__ == "__main__":
    main()
