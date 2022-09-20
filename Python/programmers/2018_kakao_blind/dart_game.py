def solution(dartResult):
    answer = []
    before_num = False
    for char in dartResult:
        if char == "S":
            before_num = False
            answer[-1] = int(answer[-1])
        elif char == "D":
            before_num = False
            answer[-1] = int(answer[-1]) ** 2
        elif char == "T":
            before_num = False
            answer[-1] = int(answer[-1]) ** 3
        elif char == "*":
            before_num = False
            if len(answer) == 1:
                answer[-1] = answer[-1] * 2
            else:
                answer[-1], answer[-2] = answer[-1] * 2, answer[-2] * 2
        elif char == "#":
            before_num = False
            answer[-1] = -answer[-1]
        else: # 숫자
            if before_num:
                answer[-1] += "0"
            else:
                answer.append(char)
            before_num = True
    return sum(answer)

dartResult = "1D2S#10S" #"1S2D*3T" # ans 37
print(solution(dartResult))