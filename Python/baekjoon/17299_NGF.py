import sys
from collections import Counter

def main():
    n = int(sys.stdin.readline().strip())
    sequence = list(map(int, sys.stdin.readline().strip().split()))
    stack = [0]
    result = [-1] * n
    counter = Counter()
    for s in sequence:
        counter[s] += 1

    for i in range(1, n):
        while stack and counter[sequence[stack[-1]]] < counter[sequence[i]]:
            result[stack.pop()] = sequence[i]
        stack.append(i)

    for r in result:
        print(r, end=" ")


if __name__ == "__main__":
    main()

"""inputs
7
1 1 2 3 4 2 1
"""