import sys


def solution(heights):
    max_vol = 0
    start_index = 0
    max_height = 0
    stack = []
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            index = stack.pop()
            if len(stack) == 0:
                width = i
            else:
                width = (i - stack[-1] - 1)
            max_vol = max(max_vol, width * heights[index])

        stack.append(i)
    while stack:
        index = stack.pop()
        if len(stack) == 0:
            width = len(heights)
        else:
            width = (len(heights) - stack[-1] - 1)
        max_vol = max(max_vol, width * heights[index])
    return max_vol

def main():
    n = int(sys.stdin.readline().strip())
    inputs = []
    for _ in range(n):
        inputs.append(int(sys.stdin.readline().strip()))

    print(solution(inputs))

if __name__ == "__main__":
    main()


"""inputs
7
2
1
4
5
1
3
3
"""
