
import heapq
# 오른쪽, 밑, 왼쪽 위,
direction = {
    0: [0, 1],
    1: [1, 0],
    2: [0, -1],
    3: [-1, 0]
}


def solution(board):
    answer = 0

    board_size = len(board)

    visited = [[[False,False,False,False] for _ in range(board_size+1)] for _ in range(board_size + 1)]
    changed_time = [[0] * len(board)  for _ in range(len(board) + 1)]
    hq = []
    heapq.heappush(hq, (100, 0, 1, 0))
    heapq.heappush(hq, (100, 1, 0, 1))
    for i in range(4):
        visited[0][0][i] = True
    # print(visited)

    while hq:
        # 비용, 꺽인 횟수, y, x, 이전 방향
        cost, y, x, prev_dir = heapq.heappop(hq)
        if y >= board_size or y < 0 or x >= board_size or x < 0:
            continue
        # 겹치면
        if visited[y][x][prev_dir]:
            continue
        visited[y][x][prev_dir] = True

        if board[y][x] == 1:
            continue
        print(cost, y, x, prev_dir)
        if y == board_size - 1 and x == board_size - 1:
            return cost
        for i in range(4):
            dy, dx = y + direction[i][0], x + direction[i][1]
            if i == prev_dir:
                heapq.heappush(hq, (cost + 100, dy, dx, i))
            else:
                heapq.heappush(hq, (cost + 600, dy, dx, i))

    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))