import sys
import heapq

def main():
    N = int(sys.stdin.readline().strip())
    hq = []
    for i in range(N):
        K = int(sys.stdin.readline().strip())
        if K == 0:
            if hq:
                print(heapq.heappop(hq)[1])
            else:
                print(0)
        else:
            heapq.heappush(hq, (abs(K), K))


if __name__ == "__main__":
    main()
