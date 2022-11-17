import sys

sys.setrecursionlimit(100000)
def main():
    n = int(sys.stdin.readline().strip())
    w = int(sys.stdin.readline().strip())
    crimes = [[0,0]]
    for _ in range(w):
        crimes.append(list(map(int, sys.stdin.readline().strip().split())))
    # 그리디하게 오답
    """
    6
    2
    3 3
    1 1
    """
    """
    crimes = []
    ret = []
    answer = 0
        for _ in range(w):
        crimes.append(list(map(int, sys.stdin.readline().strip().split())))
    man_y, man_x = 1, 1
    girl_y, girl_x = n, n
    for crime_y, crime_x in crimes:
        man_movement = abs(crime_y - man_y) + abs(crime_x - man_x)
        girl_movement = abs(crime_y - girl_y) + abs(crime_x - girl_x)
        if man_movement >= girl_movement:
            ret.append(2)
            girl_y = crime_y
            girl_x = crime_x
            answer += girl_movement
        else:
            ret.append(1)
            answer += man_movement
            man_y = crime_y
            man_x = crime_x

    print(answer)
    for r in ret:
        print(r)
    """
    # dp
    # i -> 1번 경찰차가 마지막으로 해결한 사건일때 최소거리
    # j -> 2번 경찰차가 마지막으로 해결한 사건일때 최소거리
    dp = [[-1] * (w + 1) for _ in range(w + 1)]
    def solve(i, j):
        """
        :param i: 경찰차 1이 마지막 i번째 를 처리함
        :param j: 경차차 2가 마지막 j번째 를 처리함
        :return: 이동거리 최솟값
        """

        if i == w or j == w:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        next = max(i, j) + 1 # 다음 사건
        if i == 0:
            disti = abs(crimes[next][0] - 1) + abs(crimes[next][1] - 1)
        else:
            disti = abs(crimes[next][0] - crimes[i][0]) + abs(crimes[next][1] - crimes[i][1])

        if j == 0:
            distj = abs(crimes[next][0] - n) + abs(crimes[next][1] - n)
        else:
            distj = abs(crimes[next][0] - crimes[j][0]) + abs(crimes[next][1] - crimes[j][1])

        left = solve(next, j) + disti
        right = solve(i, next) + distj
        dp[i][j] = min(left, right)
        # print(i, j, left, right, dp[i][j])
        return dp[i][j]


    def back(i, j):
        if i == w or j == w:
            return
        next = max(i, j) + 1  # 다음 사건
        if i == 0:
            disti = abs(crimes[next][0] - 1) + abs(crimes[next][1] - 1)
        else:
            disti = abs(crimes[next][0] - crimes[i][0]) + abs(crimes[next][1] - crimes[i][1])
        if j == 0:
            distj = abs(crimes[next][0] - n) + abs(crimes[next][1] - n)
        else:
            distj = abs(crimes[next][0] - crimes[j][0]) + abs(crimes[next][1] - crimes[j][1])
        # print(i, j, next)
        if dp[i][next] + distj < dp[next][j] + disti:
            print(2)
            back(i, next)
        else:
            print(1)
            back(next, j)

    print(solve(0, 0))
    back(0, 0)

if __name__ == "__main__":
    main()

"""
6
3
3 5
5 5
2 3
"""
