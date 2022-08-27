import collections


def check(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            continue
        else:
            count += 1
        if count == 2:
            return False
    return True


def solution(begin, target, words):
    if begin == target:
        return 0
    if target not in words:
        return 0
    answer = 0
    graph = collections.defaultdict(list)
    words.append(begin)
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            if check(words[i], words[j]):
                graph[words[i]].append(words[j])
    q = collections.deque()
    q.append((begin, 0))
    visited = []
    while q:
        node, count = q.popleft()
        if node == target:
            return count
        if node not in visited:
            visited.append(node)
            for next in graph[node]:
                q.append([next, count + 1])

    return 0