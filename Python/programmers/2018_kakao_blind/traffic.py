import datetime


def solution(lines):
    log = []
    for line in lines:
        logs = line.split(" ")
        timestamp = datetime.datetime.strptime(logs[0] + " " + logs[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        log.append((timestamp, -1))
        log.append(((timestamp - float(logs[2][:-1]) + 0.001), 1))

    log.sort(key=lambda x:x[0])
    accumulated = 0
    max_request = 1
    for idx, time1 in enumerate(log):
        current = accumulated
        for time2 in log[idx:]:
            if time2[0] - time1[0] > 0.999:
                break
            if time2[1] > 0:
                current += 1
        max_request = max(max_request, current)
        accumulated += time1[1]

    return max_request


lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]

print(solution(lines))
