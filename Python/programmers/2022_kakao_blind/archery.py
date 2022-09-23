import itertools
from collections import Counter

def solve(apeach, ryan) -> int:
    apeach_score = 0
    ryan_score = 0
    for i in range(1, 11):
        if apeach[i] or ryan[i]:
            if apeach[i] < ryan[i]:
                ryan_score += i
            else:
                apeach_score += i
    return ryan_score - apeach_score

def solution(n, info):
    answer = [-1]
    apeach_counter = dict([(10 - i, cnt) for (i, cnt) in enumerate(info) if cnt > 0])
    apeach_counter = Counter(apeach_counter)
    max_diff = float("-inf")
    # print(apeach_counter)
    for i in itertools.combinations_with_replacement([0,1,2,3,4,5,6,7,8,9,10], n):
        ryan_counter = Counter(i)
        # print(ryan_counter)
        # print(solve(apeach_counter, ryan_counter))
        diff = solve(apeach_counter, ryan_counter)
        if diff > max_diff and diff > 0:
            max_diff = diff
            answer = [0] * 11
            # print(ryan_counter)
            for key in ryan_counter:
                answer[10 - key] = ryan_counter[key]

    return answer

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n,info))