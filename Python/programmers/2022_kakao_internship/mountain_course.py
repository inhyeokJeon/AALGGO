# 등산코스에서 출입구는 처음과 끝에 한 번씩, 산봉우리는 한 번만 포함되어야 합니다.
from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for path in paths:
        graph[path[0]].append((path[2], path[1]))
        graph[path[1]].append((path[2], path[0]))
    q = []
    node_intensity_info = [float("inf")] * (n + 1)
    for gate in gates:
        heapq.heappush(q, (0, gate))
        node_intensity_info[gate] = 0

    while q:
        intense, node = heapq.heappop(q)
        if node in summits or intense > node_intensity_info[node]:
            continue
        for w, v in graph[node]:
            intensity = max(w, intense)
            if intensity < node_intensity_info[v]:
                node_intensity_info[v] = intensity
                heapq.heappush(q, (intensity, v))
    answer = []
    for summit in summits:
        answer.append([summit, node_intensity_info[summit]])
    answer.sort(key=lambda x: (x[1], x[0]))
    return answer[0]

n = 6
n = 7
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
gates = [1, 3]
gates = [1]
summits = [5]
summits = [2,3,4]
print(solution(n,paths,gates,summits))