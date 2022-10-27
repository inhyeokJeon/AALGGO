import sys

def solution():
    N, K = list(map(int,sys.stdin.readline().strip().split()))
    peoples = [i for i in range(1, N+1)]
    length = N
    start = K - 1
    result = []
    if K == 1:
        result = peoples
        print("<", end="")
        for r in result[:-1]:
            print(r, end=", ")
        print(result[-1], end=">")
        return
    while peoples:
        result.append(peoples.pop(start))
        length -= 1
        start = (start + (K - 1)) % length
        # print(length)
        if len(peoples) == 1:
            break
    result.append(peoples.pop())
    print("<", end="")
    for r in result[:-1]:
        print(r, end=", ")
    print(result[-1], end=">")

solution()
