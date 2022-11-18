import sys

def main():
    n = int(sys.stdin.readline().strip())

    sequence = list(map(int, sys.stdin.readline().strip().split()))
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    max_length = max(dp)
    ret = max_length
    idx = dp.index(max_length)
    result = []
    for i in range(idx, -1, -1):
        if max_length - 1 == dp[i]:
            result.append(sequence[i])
            max_length -= 1

    print(ret)
    print(*reversed(result), sequence[idx])
if __name__ == "__main__":
    main()

"""
7
3 1 5 2 3 6 4
"""

"""
8
30 1 9 40 7 5 4 90
"""