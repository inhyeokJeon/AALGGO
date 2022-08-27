from collections import defaultdict


def solution(gems):
    size = len(set(gems))
    full_size = len(gems)
    if size == 1 or len(gems) == 1:
        return [1, 1]
    min_val = 100001
    start = 0
    end = full_size - 1
    count = 50000
    ret = []
    right_start = 0
    right_end = full_size - 1
    # right first
    while len(set(gems[right_start:right_end + 1])) == size:
        right_end -= 1
    right_end += 1

    while len(set(gems[right_start:right_end + 1])) == size:
        right_start += 1
    right_start -= 1

    left_start = 0
    left_end = full_size - 1
    right_result = right_end - right_start
    # left first
    while len(set(gems[left_start:left_end + 1])) == size:
        left_start += 1
    left_start -= 1

    while len(set(gems[left_start:left_end + 1])) == size:
        left_end -= 1
    left_end += 1
    left_result = left_end - left_start
    if left_result < right_result:
        return (left_start+1, left_end+1)
    else:
        return (right_start+1, right_end+1)


print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["A", "B", "B", "B", "B", "B", "B", "C", "B", "A"]))
