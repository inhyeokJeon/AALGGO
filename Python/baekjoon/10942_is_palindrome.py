import sys

def main():
    N = int(sys.stdin.readline().strip())
    numbers = [0] + list(map(int, sys.stdin.readline().strip().split()))
    M = int(sys.stdin.readline().strip())
    dp = [[0] * (N + 1) for _ in range(N + 1)] # i번째 에서 j번째 까지 곱한 것
    for i in range(1, N+1):
        dp[i][i] = 1
    for i in range(1, N):
        if numbers[i] == numbers[i+1]:
            dp[i][i + 1] = 1



    for i in range(3, N + 1):
        for j in range(1, N - i + 2):
            if dp[j + 1][j + i - 2] and numbers[j] == numbers[j + i - 1]:
                dp[j][j + i - 1] = 1
            # if i % 2 == 0: # 짝수일 경우
            #
            #         dp[j][j + i - 1] = True
            # else: # 홀수일경우
            #     if dp[j + 1][j + i - 2] and
            #         dp[j][j + i - 1] = True
    for i in range(M):
        start, end = list(map(int, sys.stdin.readline().strip().split()))
        print(dp[start][end])
    # for d in dp:
    #     print(d)


if __name__ == "__main__":
    main()


"""inputs
7
1 1 1 3 1 1 1
4
1 3
2 5
3 3
5 7
"""
