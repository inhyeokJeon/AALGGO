import sys





def main():
    n = int(sys.stdin.readline().strip())
    inputs = []
    for _ in range(n):
        inputs.append(int(sys.stdin.readline().strip()))

    def solution():
        stack = []
        answer = 0
        for i in range(n):
            while stack and stack[-1][0] < inputs[i]:
                answer += stack.pop()[1]
            if not stack: # 내가 제일 크다.
                stack.append((inputs[i], 1))
            elif stack[-1][0] == inputs[i]: # 같을떄 큰사람이 보면 같은 수 만큼 더해줘야하기 때문에.
                count = stack.pop()[1]
                answer += count
                if stack:
                    answer += 1
                stack.append((inputs[i], count + 1))
            else: # 작은 사람
                stack.append((inputs[i], 1))
                answer += 1
        return answer
    print(solution())


if __name__ == "__main__":
    main()


"""inputs
7
2
4
1
2
2
1
5
"""

"""
5
4
5
2
3
1
"""