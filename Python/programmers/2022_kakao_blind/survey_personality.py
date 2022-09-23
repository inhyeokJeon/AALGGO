from collections import defaultdict

def solution(survey, choices):
    answer = ''
    dict = defaultdict(int)
    temp = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    def check(category, choice):
        first_cate = category[0]
        second_cate = category[1]
        if choice > 4:
            dict[second_cate] += temp[choice]
        elif choice < 4:
            dict[first_cate] += temp[choice]
    for i in range(len(survey)):
        check(survey[i], choices[i])
    if dict["R"] < dict["T"]:
        answer += "T"
    else:
        answer += "R"
    if dict["C"] < dict["F"]:
        answer += "F"
    else:
        answer += "C"
    if dict["J"] < dict["M"]:
        answer += "M"
    else:
        answer += "J"
    if dict["A"] < dict["N"]:
        answer += "N"
    else:
        answer += "A"
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
survey = ["TR", "RT", "TR"]
choices = [5, 3, 2, 7, 5]
choices = [7,1,3]
print(solution(survey, choices))