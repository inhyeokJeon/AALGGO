import sys
from collections import deque
T = int(sys.stdin.readline().strip())

for _ in range(T):
    N, K = list(map(int, sys.stdin.readline().strip().split()))
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    dq = deque()

    for i in range(N):
        dq.append((numbers[i], i))
    count = 1
    while dq:
        max_val = max(dq, key=lambda x: x[0])

        while max_val[0] != dq[0][0]:
            dq.append(dq.popleft())
        val, idx = dq.popleft()
        if K == idx:
            print(count)
            break
        count += 1
