import sys

N, K = list(map(int, sys.stdin.readline().strip().split()))
# 북 동 남 서
dir_y = [-1, 0, 1, 0]
dir_x = [0, 1, 0, -1]
def step1(blocks):
    minimum = min(blocks)
    for i in range(N):
        if blocks[i] == minimum:
            blocks[i] += 1
    return blocks

def step2(blocks):
    result = []
    count, many = 0, 1
    if not blocks:
        return result
    while True:
        count += 1
        temp = []
        for i in range(many):
            temp.append(blocks.pop(0))
        result.append(temp)
        if count == 2:
            # print("회전한 result", result)
            many += 1
            count = 0
        if len(blocks) < many:
            break
        result = list(map(list, zip(*result[::-1])))
    result[-1] += blocks
    return result

def step3(blocks):
    # print("in step3", blocks)
    cand = []
    visited = set()
    for i in range(len(blocks)):
        for j in range(len(blocks[0])):
            for d in range(4):
                next_i, next_j = i + dir_y[d], j + dir_x[d]
                if next_i < 0 or next_j < 0 or next_i >= len(blocks) or next_j >= len(blocks[0]) or (next_i, next_j) in visited:
                    continue
                visited.add((i, j))
                if abs(blocks[i][j] - blocks[next_i][next_j]) // 5 > 0:
                    if (blocks[i][j] - blocks[next_i][next_j]) > 0: # blocks[i][j] 가 더크면
                        cand.append((i, j, - (abs(blocks[i][j] - blocks[next_i][next_j]) // 5)))
                        cand.append((next_i, next_j, (abs(blocks[i][j] - blocks[next_i][next_j]) // 5)))
                    else:
                        cand.append((i, j, (abs(blocks[i][j] - blocks[next_i][next_j]) // 5)))
                        cand.append((next_i, next_j, - (abs(blocks[i][j] - blocks[next_i][next_j]) // 5)))
    visited = set()
    # 맨밑에 남은 피자 도우들
    if len(blocks[0]) < len(blocks[-1]):
        for i in range(len(blocks[0]), len(blocks[-1])):
            if abs(blocks[-1][i-1] - blocks[-1][i]) // 5 > 0:
                if (blocks[-1][i-1] - blocks[-1][i]) > 0:  # blocks[-1][i-1] 가 더크면
                    cand.append((-1, i - 1, - (abs(blocks[-1][i-1] - blocks[-1][i]) // 5)))
                    cand.append((-1, i, (abs(blocks[-1][i-1] - blocks[-1][i]) // 5)))
                else:
                    cand.append((-1, i - 1, (abs(blocks[-1][i-1] - blocks[-1][i]) // 5)))
                    cand.append((-1, i, - (abs(blocks[-1][i-1] - blocks[-1][i]) // 5)))
    for r, c, num in cand:
        blocks[r][c] += num
    return blocks

def step4(blocks):
    result = []
    temp_block = list(map(list, zip(*blocks[::-1])))
    while temp_block:
        temp = temp_block.pop(0)
        result += temp
    if len(blocks[0]) < len(blocks[-1]):
        result += blocks[-1][len(blocks[0]):]
    return result

def step5(blocks):
    mid = N // 2
    temp = []
    left, right = blocks[:mid], blocks[mid:]
    # print("left", left, "right", right)
    temp.append(left[::-1])
    temp.append(right)
    temp_left = []
    temp_right = []
    for i in range(2):
        temp_left.append(temp[i][:mid // 2])
        temp_right.append(temp[i][mid // 2:])
    temp_left = list(map(list, zip(*temp_left[::-1])))
    temp_left = list(map(list, zip(*temp_left[::-1])))
    return temp_left + temp_right

def check(blocks):
    return (max(blocks) - min(blocks)) <= K

def solution():
    blocks = list(map(int, sys.stdin.readline().strip().split()))
    count = 1
    while True:
        after_step1 = step1(blocks)
        # print(after_step1)
        after_step2 = step2(after_step1)
        # print(after_step2)
        after_step3 = step3(after_step2)
        # print("step3",after_step3)
        after_step4 = step4(after_step3)
        # print("step4", after_step4)
        after_step5 = step5(after_step4)
        # print(after_step5)
        after_step6 = step3(after_step5)
        # print("step6", after_step6)
        after_step7 = step4(after_step6)
        # print("step7", after_step7)
        blocks = after_step7

        if check(after_step7):
            break
        count += 1
    return count
print(solution())
"""inputs
8 4
1 10 4 13 8 3 1 7
"""