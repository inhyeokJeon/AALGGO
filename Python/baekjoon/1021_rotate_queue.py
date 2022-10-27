import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().strip().split()))
needs = list(map(int, sys.stdin.readline().strip().split()))
numbers = [i for i in range(1, N+1)]
dq = deque(numbers)
def check(queue, need, count):
    # 종료 조건 필요한 것이 없을때

    if need == K:
        return count
    idx = queue.index(needs[need])
    # print(queue, need, count, needs[need], idx)
    if idx > len(queue) // 2: # 오른쪽 회전이 나음
        queue.rotate(len(queue) - idx)
        queue.popleft()
        # print("right", len(queue) - idx + 1)
        return check(queue, need + 1, count + len(queue) - idx + 1)
    else:
        queue.rotate(-idx)
        queue.popleft()
        # print("left", idx)
        return check(queue, need + 1, count + idx)

print(check(dq, 0, 0))
