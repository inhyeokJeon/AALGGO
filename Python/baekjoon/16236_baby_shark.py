"""
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.

아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.
"""
import sys
import heapq
N = int(sys.stdin.readline().strip())
blocks = [[0] * (N) for _ in range(N)] # blocks
dir_y = [-1, 0, 0, 1] # 북 서 동 남
dir_x = [0, -1, 1, 0]
# shark_y, shark_x = 0, 0

for i in range(N):
    blocks[i] = list(map(int, sys.stdin.readline().strip().split()))


def check_fish(shark_kg):
    for i in range(N):
        for j in range(N):
            if 0 < blocks[i][j] < shark_kg:
                return True
    return False


def check_first_shark_position():
    for i in range(N):
        for j in range(N):
            if blocks[i][j] == 9:
                blocks[i][j] = 0
                return i, j


def out_of_range(y,x):
    return y < 0 or x < 0 or y >= N or x >= N


def solve(shark_y, shark_x, shark_kg):
    # killed = [(shark_y, shark_x)] # 잡았떤 곳은 다시 가지않기 위해
    result = 0
    # isEating = False
    eating_count = 0
    while True: # 먹을 수 있는 물고기가 있으면 계속 반복
        # if not check_fish(shark_kg):
        #     break
        q = []
        visited = set((shark_y, shark_x))
        heapq.heappush(q, (0, shark_y, shark_x))
        catch = False
        while q:
            now_d, now_y, now_x = heapq.heappop(q)
            if 0 < blocks[now_y][now_x] < shark_kg: # 상어가 잡아 먹을 수 있따면
                eating_count += 1
                shark_y, shark_x = now_y, now_x
                result += now_d
                blocks[now_y][now_x] = 0
                # isEating = True
                if eating_count == shark_kg:
                    shark_kg += 1
                    eating_count = 0
                # print(shark_y + 1, shark_x + 1)
                # killed.append((shark_y, shark_x))
                catch = True
                break
            for i in range(4):
                next_y, next_x = now_y + dir_y[i], now_x + dir_x[i]
                if out_of_range(next_y, next_x) or (next_y, next_x) in visited or blocks[next_y][next_x] > shark_kg:
                    continue
                heapq.heappush(q, (now_d + 1, next_y, next_x))
                visited.add((next_y, next_x))
                # q.append()
        if not catch:
            break
        # if not isEating and (shark_y == 0, shark_x == 0):
        #     break
        # print("shark_kg", result, shark_kg, shark_y, shark_x)
        # for i in blocks:
        #     print(i)
    return result


def main():
    shark_y, shark_x = check_first_shark_position()
    print(solve(shark_y, shark_x, 2))
main()
# hq = []
# test = [(1,1,1), (1,2,1), (1,1,1), (1,2,2), (1,2,3)]
# for t in test:
#     heapq.heappush(hq, t)
#
# while hq:
#     print(heapq.heappop(hq))

"""
5
0 0 5 0 0
0 6 1 7 0
8 2 0 3 10
0 9 4 11 0
0 0 12 0 0
"""