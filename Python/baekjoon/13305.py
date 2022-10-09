import sys

N = int(sys.stdin.readline().strip())

distances = list(map(int, sys.stdin.readline().strip().split()))
fees = list(map(int, sys.stdin.readline().strip().split()))
answer = 0
minimum = min(fees[:-1])
while distances:
    dist = distances.pop()
    fee = fees.pop()
    if minimum == fee:
        minimum = min(fees)
    answer += (minimum * dist)

print(answer)