from collections import defaultdict


def solution(record):
    answer = []
    real_answer = []
    name_dict = defaultdict(str)
    for rec in record:
        records = rec.split(" ")
        if records[0] == "Enter": # 들어왔으면 1
            name_dict[records[1]] = records[2]
            answer.append((records[1], True))
        elif records[0] == "Leave": # 나가면 2
            answer.append((records[1], False))
        elif records[0] == "Change": # 바꾸면 딕트만 바꿈
            name_dict[records[1]] = records[2]
    for id, is_enter in answer:
        if is_enter:
            real_answer.append(f"{name_dict[id]}님이 들어왔습니다.")
        else:
            real_answer.append(f"{name_dict[id]}님이 나갔습니다.")

    return real_answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))