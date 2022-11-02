import sys
def solution(N, K):
    left = 1
    right = K
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for i in range(1, N + 1):
            count += min(mid // i, N)
        if count < K:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
    return ans


def main():
    N = int(sys.stdin.readline().strip())
    K = int(sys.stdin.readline().strip())
    print(solution(N, K))

if __name__ == "__main__":
    main()
"""
5
7
"""
