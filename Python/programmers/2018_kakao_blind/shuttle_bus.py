def solution(n, t, m, timetable) -> str:
    """
    :param n: 버스 운행 횟수
    :param t: 버스 운행 간격
    :param m: 버스 탑승 인원
    :param timetable: time table
    :return: 콘이 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각 ex "09:00"
    """
    timetable = [int(time.split(":")[0]) * 60 + int(time.split(":")[1]) for time in timetable]
    timetable.sort()
    current = 540 # 9시
    for i in range(n):
        for j in range(m):
            if timetable and timetable[0] <= current:
                candidate = timetable.pop(0) - 1
            else:
                candidate = current
        current += t
    result = divmod(candidate, 60)
    result = str(result[0]).zfill(2) + ":" + str(result[1]).zfill(2)
    return result



n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n,t,m,timetable))