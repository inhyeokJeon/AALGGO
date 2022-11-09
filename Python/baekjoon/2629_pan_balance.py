import sys

def main():
    N = int(sys.stdin.readline().strip())
    weights = [0] + list(map(int, sys.stdin.readline().strip().split()))
    M = int(sys.stdin.readline().strip())
    tests = list(map(int, sys.stdin.readline().strip().split()))
    weight_sum = sum(weights)
    dp = [[False] * (weight_sum + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        weight = weights[i]
        dp[i][weight] = True
        for j in range(1, weight_sum + 1): # weight
            if dp[i-1][j]:
                dp[i][j] = True
                dp[i][abs(j - weight)] = True
                if weight + j <= (weight_sum):
                    dp[i][weight + j] = True

    for t in tests:
        if t > weight_sum:
            print("N", end=" ")
        elif dp[-1][t]:
            print("Y", end=" ")
        else:
            print("N", end=" ")

if __name__ == "__main__":
    main()


"""inputs
4
2 3 3 3
3
1 4 10
"""
