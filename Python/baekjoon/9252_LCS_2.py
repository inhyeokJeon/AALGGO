import sys


def main():
    l1 = sys.stdin.readline().strip()
    l2 = sys.stdin.readline().strip()
    dp = [[0] * (len(l2) + 1) for _ in range(len(l1) + 1)]
    for i in range(1, len(l1) + 1):
        for j in range(1, len(l2) + 1):
            if l1[i - 1] == l2[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    row = len(l1)
    col = len(l2)
    temp_val = 0
    result = ""
    while row != 0 and col != 0:
        if dp[row][col] == dp[row - 1][col]:
            row -= 1
        elif dp[row][col] == dp[row][col - 1]:
            col -= 1
        else: # 왼쪽 위 값만 다르다.
            result += l1[row - 1]
            col -= 1
            row -= 1

    if result:
        print(len(result))
        print(result[::-1])
    else:
        print(0)
if __name__ == "__main__":
    main()

"""
KKKBCBCAAA
KCKBCBCAKK
"""
