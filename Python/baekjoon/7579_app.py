import sys
MOD = 2_000_000_000
def main():
    N, M = list(map(int, sys.stdin.readline().strip().split()))

    apps = list(map(int, sys.stdin.readline().strip().split()))
    costs = list(map(int, sys.stdin.readline().strip().split()))
    # apps_costs = []
    # for i in range(N):
    #     apps_costs.append([apps[i], costs[i]])
    # apps_costs.sort(reverse=True)
    # print(apps_costs)
    sum_cost = sum(costs)
    dp = [[0] * (sum_cost + 1) for _ in range(N + 1)]
    # row N개 col 바이트 수
    result = sum_cost
    for i in range(1, N + 1):
        memory = apps[i - 1]
        cost = costs[i - 1]
        for j in range(1, sum_cost + 1):
            if j < cost:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - cost] + memory, dp[i - 1][j])

            if dp[i][j] >= M:
                result = min(result, j)

    print(result)

if __name__ == "__main__":
    main()


"""inputs
3 10
1
2
5
"""
