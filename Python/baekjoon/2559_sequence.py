import sys
from copy import deepcopy
N, K = list(map(int,sys.stdin.readline().strip().split()))
number = list(map(int,sys.stdin.readline().strip().split()))
prefix_sum = deepcopy(number)
for i in range(1, N):
    prefix_sum[i] = number[i] + prefix_sum[i-1]
result = prefix_sum[K - 1]
for i in range(N - K):
    result = max(result, prefix_sum[i + K] - prefix_sum[i])

print(result)