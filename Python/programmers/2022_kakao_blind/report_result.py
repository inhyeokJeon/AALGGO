from collections import OrderedDict, defaultdict


def solution(id_list, report, k):
    answer = []
    temp = OrderedDict()
    temp2 = defaultdict(set)
    ret = defaultdict(int)
    for id in id_list:
        temp[id] = 0
    for repo in report:
        all = repo.split()
        do = all[0]
        get = all[1]
        if get in temp2[do]:
            continue
        temp2[do].add(get)
        temp[get] += 1

    for id in temp:
        if temp[id] < k:
            # print("condtinue id :", id)
            continue
        for second in temp2:
            if id in temp2[second]:
                ret[second] += 1

    for id in id_list:
        answer.append(ret[id])
    # print(temp)
    # print(temp2)
    # print(ret)

    return answer