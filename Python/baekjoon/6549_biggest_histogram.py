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
    while True:
        inputs = list(map(int, sys.stdin.readline().strip().split()))
        if len(inputs) == 1 and inputs[0] == 0:
            break
        else:
            inputs = inputs[1:]
            print(solution(inputs))

if __name__ == "__main__":
    main()


"""inputs
7 2 1 4 5 1 3 3
6 1 2 3 4 5 1
5 5 4 3 2 1
0
"""
