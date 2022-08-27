import collections


def solution(tickets):
    answer = []
    # 모든 경로 저장
    # 모든 경로 중 tickets + 1 이면서 알파벳 순서가 제일 빠른것
    gragh = collections.defaultdict(list)

    for start, end in sorted(tickets):
        gragh[start].append(end)

    def dfs(a):
        while gragh[a]:
            dfs(gragh[a].pop(0))
        answer.append(a)

    dfs("ICN")

    return answer[::-1]