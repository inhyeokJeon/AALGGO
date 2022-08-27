# 한 번에 한 명씩 신청한 순서대로 방을 배정합니다.
# 고객은 투숙하기 원하는 방 번호를 제출합니다.
# 고객이 원하는 방이 비어 있다면 즉시 배정합니다.
# 고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정합니다.
from collections import defaultdict

def solution(k, room_number):
    answer = []
    rooms = []
    available = []
    temp = defaultdict(int)
    for i in range(1, 200001):
        available.append(i)
    for idx, room in enumerate(room_number):
        if not temp[room]:
            if room > 200000:
                temp[room] = room
                answer.append(room)
            else:
                temp[room] = room
                answer.append(room)
                index = available.index(room)
                available[index] = float('inf')
        else:
            min_val = min(available[room:2000001])
            min_index = available.index(min_val)
            available[min_index] = float('inf')
            answer.append(min_val)

    return answer
# def solution(k, room_number):
#     answer = []
#     rooms = []
#     df = defaultdict(list)
#     for i in range(0, 200001):
#         df[i] = [i-1, i+1]
#     # print(df)
#     # for i in range(1, k + 1):
#     #     rooms.append(i)
#
#     temp = defaultdict(int)
#     deleted = []
#
#     for idx, room in enumerate(room_number):
#         now_min = df[0][1]
#         if room > 200000:
#             # 방문한 적 없으면
#             if not temp[room]:
#                 temp[room] = room
#                 answer.append(room)
#             # 방문한 적 있으면
#             else:
#                 # 이전 방은 현재의 다음 방을 가르킴
#                 df[df[now_min][0]][1] = df[now_min][1]
#                 # 다음 방은 현재의 이전방을 가르킴
#                 df[df[now_min][1]][0] = df[now_min][0]
#                 temp[now_min] = now_min
#                 answer.append(now_min)
#
#         else:
#             # 방문한 적 없으면
#             if not temp[room]:
#                 # 이전 방은 현재의 다음 방을 가르킴
#                 df[df[room][0]][1] = df[room][1]
#                 # 다음 방은 현재의 이전방을 가르킴
#                 df[df[room][1]][0] = df[room][0]
#                 temp[room] = room
#                 answer.append(room)
#             # 방문한 적 있으면
#             else:
#                 df[df[now_min][0]][1] = df[now_min][1]
#                 # 다음 방은 현재의 이전방을 가르킴
#                 df[df[now_min][1]][0] = df[now_min][0]
#                 temp[now_min] = now_min
#                 answer.append(now_min)

    #
    # print(df)
    # print(temp)
        # 방 안팔렸으면
        # if room in rooms:
        #     temp = rooms.index(room)
        #     answer.append(rooms.pop(temp))
        # else: # 방 팔렸으면
        #     answer.append(rooms.pop(0))

        # if rooms[room] == 0:
        #     first = rooms[]
        #     rooms[first] = '1'
        #     answer.append(first)
        # else:
        #     rooms[room] = '1'
        #     answer.append(room)
    # return answer

print(solution(10, [1,3,4,1,3,1]))