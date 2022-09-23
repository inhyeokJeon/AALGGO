from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    dict = defaultdict(list)
    for record in records:
        rec = record.split(" ")
        time = rec[0].split(":")
        if rec[2] == "IN":
            dict[rec[1]].append(int(time[0]) * 60 + int(time[1]))
        else:
            dict[rec[1]].append(int(time[0]) * 60 + int(time[1]))

    for i in sorted(dict.keys()):
        total_time = 0
        total_cost = 0
        # print(dict[i])
        if len(dict[i]) % 2 == 1: # 출차 없으면
            time = dict[i].pop()
            total_time = (1439 - time)

        for j in range(0, len(dict[i]), 2):
            total_time += (dict[i][j+1] - dict[i][j])
        # print(total_time)
        if total_time > fees[0]:
            total_cost += fees[1]
            total_time -= fees[0]
            total_cost += (math.ceil(total_time / fees[2]) * fees[3])
        else:
            total_cost = fees[1]

        answer.append(total_cost)

    return answer

fees = [180, 5000, 10, 600]
fees = [120, 0, 60, 591]
fees = [1, 461, 1, 10]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
records = ["00:00 1234 IN"]
print(solution(fees, records))