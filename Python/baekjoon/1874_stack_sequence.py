import sys
N = int(sys.stdin.readline().strip())
inputs = []

for _ in range(N):
    inputs.append(int(sys.stdin.readline().strip()))

result = []
ordered = [i for i in range(1, N + 1)]
stack = []
count = 0
# print(ordered)
# print(inputs)
number = 0 # 기준
for char in inputs:
    if not stack: # 스택이 비었으면
        for num in range(number + 1, char + 1):
            stack.append(num)
            result.append("+")
        number = char
    if stack[-1] == char:
        stack.pop()
        result.append("-")
    elif stack[-1] < char:
        for i in range(number + 1, char + 1):
            stack.append(i)
            result.append("+")
        stack.pop()
        result.append("-")
        number = char
    else:
        result = ["NO"]
        break

for r in result:
    print(r)
