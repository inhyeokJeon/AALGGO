import sys
import heapq
MAX = 200_000
def main():
    n, k = list(map(int, sys.stdin.readline().strip().split()))

    visited = [False] * (MAX + 1)
    def bfs(i):
        q = []
        heapq.heappush(q, (0, i))
        ret = float("inf")
        while q:
            count, node = heapq.heappop(q)
            if visited[node]:
                continue
            if node == k:
                return min(count, ret)
            visited[node] = True
            if node > k:
                ret = min(ret, count + node - k)
                continue
            heapq.heappush(q, (count + 1, node + 1))

            if not node - 1 < 0:
                heapq.heappush(q, (count + 1, node - 1))
            heapq.heappush(q, (count, 2 * node))
        return ret

    print(bfs(n))


if __name__ == "__main__":
    main()
