import itertools


def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
        for j in range(len(users[i])):
            if banned_id[i][j] == '*':
                continue
            elif banned_id[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    user_permutation = list(itertools.combinations(user_id, len(banned_id)))
    banned_Set = []
    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:
            print(users)
            users = set(users)
            print("set:", users)
            if users not in banned_Set:
                banned_Set.append(users)

    print(len(banned_Set))
    return len(banned_Set)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])

import itertools


def check(id_list, ban_list):
    ret = set()
    for ban in ban_list:
        ban_length = len(ban)
        sol = -1
        for i, id in enumerate(id_list):
            id_length = len(id)
            if ban_length != id_length:
                continue
            idx = 0
            while idx < id_length:
                if ban[idx] == '*':
                    idx += 1
                    continue
                if id[idx] == ban[idx]:
                    idx += 1
                    continue
                break
            # 끝까지가 같다는 것이니깐
            if idx == id_length:
                sol = i
                break
        if sol != -1:
            ret.add(id_list.pop(sol))
    return ret


def solution(user_id, banned_id):
    if len(user_id) == len(banned_id):
        return 1
    perms = list(itertools.permutations(user_id, len(user_id)))
    ret = list()
    for perm in perms:
        temp = check(list(perm), banned_id)
        if temp:
            if temp not in ret:
                ret.append(temp)

    return len(ret)
    # print(perms)


# import itertools
#
#
# def check(id_list, ban_list):
#     for i in range(len(ban_list)):
#         if len(ban_list[i]) != len(id_list[i]):
#             return False
#         for j in range(len(id_list)):
#             if ban_list[i][j] == '*':
#                 continue
#             if ban_list[i][j] != id_list[i][j]:
#                 return False
#     return True
#
#
# def solution(user_id, banned_id):
#     if len(user_id) == len(banned_id):
#         return 1
#
#     ret = []
#     for perm in list(itertools.permutations(user_id, len(banned_id))):
#         if not check(perm, banned_id):
#             continue
#         else:
#             perm = set(perm)
#             if perm not in ret:
#                 ret.append(perm)
#
#     return len(ret)