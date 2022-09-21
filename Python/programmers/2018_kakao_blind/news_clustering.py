def solution(str1, str2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    answer = 0

    def str_to_element(string: str):
        ret = []
        string = string.lower()
        for i in range(1, len(string)):
            if string[i - 1] not in alphabet or string[i] not in alphabet:
                continue
            ret.append(string[i-1] + string[i])
        return sorted(ret)

    element1 = str_to_element(str1)
    element2 = str_to_element(str2)
    element1_length = len(element1)
    element2_length = len(element2)
    point1 = 0
    point2 = 0
    intersect_counter = 0

    if element1_length == 0 and element2_length == 0:
        return 65536
    elif element1_length == 0:
        return 0
    elif element2_length == 0:
        return 0
    while point1 < len(element1) and point2 < len(element2):
        if element1[point1] < element2[point2]:
            point1 += 1
        elif element1[point1] > element2[point2]:
            point2 += 1
        else:
            point1 += 1
            point2 += 1
            intersect_counter += 1

    union_counter = element1_length + element2_length - intersect_counter
    if intersect_counter == 0:
        return 0
    if union_counter == 0:
        return 65536
    answer = int((intersect_counter / union_counter) * 65536)
    return answer

str1 = "handshake"
str2 = "shake hands"
print(solution(str1, str2))