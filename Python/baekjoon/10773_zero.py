import sys
K = int(sys.stdin.readline().strip())
number = []
for i in range(K):
    input = int(sys.stdin.readline().strip())
    if input == 0:
        number.pop()
    else:
        number.append(input)
print(sum(number))