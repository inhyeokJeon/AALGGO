import sys
from collections import deque
N = int(sys.stdin.readline().strip())
router = deque()
while True:
    num = int(sys.stdin.readline().strip())
    if num == -1:
        break
    elif num == 0:
        router.popleft()
    else:
        if len(router) < N:
            router.append(num)
if router:
    print(*router)
else:
    print("empty")
