from collections import defaultdict
from copy import deepcopy


def solution(money):
    answer = 0
    length = len(money)
    house_list = deepcopy(money)
    house_list.pop(0)
    money.pop()
    print(money)
    print(house_list)
    def solve(i):
        if i > length - 2:
            return 0
        return money[i] + max(solve(i + 2), solve(i + 3))

    def solve2(i):
        if i > length - 2:
            return 0
        return house_list[i] + max(solve2(i + 2), solve2(i + 3))

    print(max(solve(0), solve2(0)))

    return answer

print(solution([1,2,3,1]))

def solution(money):
    a1=[money[0],max(money[0],money[1])] # 0 번째, 0번째 1번째중 큰거
    a2=[money[1],max(money[1],money[2])] # 1 번째, 1번째 2번째 중 큰거.
    # a1으로 돌린 마지막 하나는 빼고 찾는다.
    for i in range(2,len(money)-1):
        a1.append(max(money[i]+a1[-2],a1[-1]))
    # a2로
    for i in range(3,len(money)):
        a2.append(max(money[i]+a2[-2],a2[-1]))
    return max(a1[-1],a2[-1])