import sys
N = int(sys.stdin.readline().strip())

time_table = []
for _ in range(N):
    start, end = list(map(int, sys.stdin.readline().strip().split()))
    time_table.append((start, end))

time_table.sort(key= lambda x: (x[1], x[0]))
# print(time_table)
now_start_time, now_end_time = time_table.pop(0)
count = 1
while time_table:
    start_time, end_time = time_table.pop(0)
    if now_end_time <= start_time:
        now_end_time = end_time
        count += 1

print(count)