import sys
def solve():
    n = int(sys.stdin.readline().strip())

    sequence = list(map(int,sys.stdin.readline().strip().split()))
    if n == 1:
        return 1
    temp = [0]
    for i in range(n):
        if sequence[i] > temp[-1]:
            temp.append(sequence[i])
        else:
            left = 1
            right = len(temp) - 1
            while left <= right:
                mid = (left + right) // 2
                if temp[mid] < sequence[i]:
                    left = mid + 1
                else:
                    right = mid - 1

            temp[left] = sequence[i]
    return len(temp) - 1
print(solve())

"""
9
10 20 30 1 2 3 4 50 60
"""