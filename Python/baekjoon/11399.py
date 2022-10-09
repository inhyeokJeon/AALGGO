import sys

N = int(sys.stdin.readline().strip())

time_table = list(map(int, sys.stdin.readline().strip().split()))
time_table.sort()

result = []
before = 0
for time in time_table:
    result.append(before + time)
    before = before + time
print(sum(result))