import sys
from copy import deepcopy
N, K = list(map(int,sys.stdin.readline().strip().split()))
number = list(map(int,sys.stdin.readline().strip().split()))
prefix_sum = deepcopy(number)
for i in range(1, N):
    prefix_sum[i] = number[i] + prefix_sum[i-1]
prefix_sum = [0] + prefix_sum
for i in range(K):
    start, end = list(map(int, sys.stdin.readline().strip().split()))
    print(prefix_sum[end] - prefix_sum[start - 1])