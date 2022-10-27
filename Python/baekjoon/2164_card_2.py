import sys
from collections import deque
N = int(sys.stdin.readline().strip())
numbers = deque([i for i in range(1, N+1)])

while len(numbers) > 1:
    front = numbers.popleft()
    numbers.append(numbers.popleft())

print(numbers[0])