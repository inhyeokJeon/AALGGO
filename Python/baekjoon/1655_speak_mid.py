import sys
import heapq
def main():
    N = int(sys.stdin.readline().strip())
    small_hq = []
    big_hq = []
    mid = int(sys.stdin.readline().strip())
    print(mid)
    for i in range(N - 1):
        K = int(sys.stdin.readline().strip())
        if K >= mid:
            heapq.heappush(big_hq, K) # 큰 얘들 중 가장 작은놈이 먼저 나오도록
        else:
            heapq.heappush(small_hq, -K) # 작은 얘들중 가장 큰놈이 먼저 나오도록

        if len(big_hq) - len(small_hq) >= 2: # 큰놈이 많을떄
            heapq.heappush(small_hq, -mid)
            mid = heapq.heappop(big_hq)
        elif len(small_hq) - len(big_hq) >= 2: # 작은놈이 많을떄
            heapq.heappush(big_hq, mid)
            mid = -heapq.heappop(small_hq)

        if i % 2 == 0: # 짝
            if len(big_hq) > len(small_hq):
                print(min(mid, big_hq[0]))
            else:
                print(min(mid, -small_hq[0]))
        else:
            print(mid)


if __name__ == "__main__":
    main()
