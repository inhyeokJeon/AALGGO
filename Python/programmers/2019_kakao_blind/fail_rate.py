from collections import defaultdict


def solution(N, stages):
    answer = []
    fail_rate = defaultdict(int)
    for num in stages:
        fail_rate[num] += 1
    now_sum = 0
    users = len(stages)
    for num in range(1, N+1):
        if users <= 0:
            answer.append((0,num))
            continue
        answer.append((fail_rate[num] / users, num))
        users -= fail_rate[num]
    answer.sort(reverse=True, key=lambda x:x[0])

    return [ans[1] for ans in answer]


n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n, stages))