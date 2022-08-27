import sys


T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    first = 1
    second = 1
    third = 1
    ret = 0
    if n == 1 or n == 2 or n == 3:
        print(1)
        continue
    for i in range(n - 3):
        ret = first + second
        first = second
        second = third
        third = ret

    print(ret)

