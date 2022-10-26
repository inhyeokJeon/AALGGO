import sys
import math
N, M = list(map(int,sys.stdin.readline().strip().split()))
number = list(map(int,sys.stdin.readline().strip().split()))
number = [0] + number
count = [0] * M

for i in range(1, N + 1):
    number[i] = (number[i] + number[i-1]) % M
    count[number[i]] += 1
result = count[0]
for val in count:
    result += val * (val - 1) // 2

print(result)


