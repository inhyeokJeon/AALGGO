import sys


def check(chosen, num) -> bool:
    """
    :param chosen: 선택된 리스트
    :param num: 기준이 되는 숫자. ex) mid
    :return: 선택된 리스트의 항의 차가 num 보다 크거나 같은 갯수
    """
    count = 1
    val = chosen[0]
    for i in range(len(chosen)):
        if chosen[i] - val >= num:
            val = chosen[i]
            count += 1
    return count

def solution(wifi, C):
    left = 1
    right = wifi[-1] - wifi[0]
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if check(wifi, mid) < C:
            right = mid - 1
        else:
            ans = mid
            left = mid + 1
    return ans

def main():
    N, C = list(map(int, sys.stdin.readline().strip().split()))
    wifi = []
    for _ in range(N):
        wifi.append(int(sys.stdin.readline().strip()))
    wifi.sort()
    print(solution(wifi, C))

if __name__ == "__main__":
    main()
"""
5 3
1
2
3
4
5
"""
