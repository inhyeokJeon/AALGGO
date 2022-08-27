from collections import defaultdict

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    # 모둔 경우의수를 키로 가지는 dict 만듬.
    for inf in info:
        lang, position, career, food, score = inf.split()
        for lan in [lang, '-']:
            for pos in [position, '-']:
                for car in [career, '-']:
                    for fo in [food, '-']:
                        info_dict[lan+pos+car+fo].append(int(score))

    # 이분탐색을 위해 정렬
    for inf in info_dict:
        info_dict[inf].sort()

    # 최대 50000개나 되기 때문에 탐색 방법을 이분탐색으로 지정.
    for q in query:
        lang, _, position, _, career, _, food, score = q.split()
        info_key = lang+position+career+food
        query_dict = info_dict[info_key]
        length = len(query_dict)
        tmp = length
        lo, hi = 0, length - 1
        score = int(score)
        while lo <= hi:
            mid = (lo + hi) // 2
            if score <= query_dict[mid]:
                tmp = mid
                hi = mid - 1
            else:
                lo = mid + 1
        answer.append(length - tmp)
    # print(info_dict, len(info_dict))

    return answer
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))