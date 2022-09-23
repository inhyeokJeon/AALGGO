from collections import Counter
import itertools

def solution(orders, course):
    ret = []
    people = len(orders)
    for order in orders:
        ret.append(Counter(order))
    result = []

    for i in course:
        temp = []
        for order in orders:
            comb = itertools.combinations(sorted(order), i)
            temp += comb

        counter = Counter(temp)
        # print(counter)
        if len(counter) != 0 and counter.most_common(1)[0][1] != 1:
            for f in counter:
                if counter[f] == counter.most_common(1)[0][1]:
                    # print(f)
                    result.append(''.join(f))
        # print(max(counter.values()))

    # print(result)
    answer = sorted(result)
    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
# course = [2,3,5]
course = [2,3,4]
print(solution(orders,course))