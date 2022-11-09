import sys

def main():
    N, K = list(map(int, sys.stdin.readline().strip().split()))

    coins = []
    for _ in range(N):
        coins.append(int(sys.stdin.readline().strip()))

    dp = [0] * (K + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, K + 1):
            dp[i] += dp[i-coin]
        print(dp)
    print(dp[-1])
if __name__ == "__main__":
    main()


"""inputs
3 10
1
2
5
"""
