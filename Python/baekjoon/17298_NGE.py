import sys


def main():
    N = int(sys.stdin.readline().strip())
    sequence = list(map(int, sys.stdin.readline().strip().split()))
    stack = [0]
    result = [-1] * N
    for i in range(1, N):
        while stack and sequence[stack[-1]] < sequence[i]:
            result[stack.pop()] = sequence[i]
        stack.append(i)

    for r in result:
        print(r, end=" ")


if __name__ == "__main__":
    main()

"""inputs
4
3 5 2 7
"""