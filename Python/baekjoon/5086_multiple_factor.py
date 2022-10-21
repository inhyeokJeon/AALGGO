import sys

while True:
    result = 0
    f, s = list(map(int, sys.stdin.readline().strip().split()))
    if f == 0 and s == 0:
        break
    if f > s:
        if f % s == 0:
            print("multiple")
        else:
            print("neither")
    else:
        if s % f == 0:
            print("factor")
        else:
            print("neither")