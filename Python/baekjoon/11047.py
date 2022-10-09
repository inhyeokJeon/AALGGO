import sys
from bisect import bisect_right
N, K = list(map(int, sys.stdin.readline().strip().split()))

coin_list = []
for _ in range(N):
    coin_list.append(int(sys.stdin.readline().strip()))

temp = bisect_right(coin_list, K)
coin_list = coin_list[:temp][::-1]
need = K
coin_index = 0
count = 0
while coin_index < len(coin_list):
    quot, remainder = divmod(need, coin_list[coin_index])
    need = remainder
    count += quot
    if need == 0:
        break
    coin_index += 1

print(count)