def solution(queue1, queue2):
    answer = -1
    expected_sum = (sum(queue1) + sum(queue2)) // 2
    one_sum = sum(queue1)
    two_sum = sum(queue2)
    i, j, length = 0, 0, len(queue1) # i 는 첫번재, j 는 두번째
    while i < length * 2 and j < length * 2 and one_sum != two_sum:
        if one_sum < expected_sum:
            one_sum += queue2[j]
            two_sum -= queue2[j]
            queue1.append(queue2[j])
            j += 1
        else:
            one_sum -= queue1[i]
            two_sum += queue1[i]
            queue2.append(queue1[i])
            i += 1
    if one_sum == expected_sum:
        answer = i + j
    return answer

queue1 = [3, 2, 7, 2]
queue1 = [1, 2, 1, 2]
# queue1 = [1,1]
queue2 = [4, 6, 5, 1]
queue2 = [1, 10, 1, 2]
# queue2 = [1,5]
print(solution(queue1,queue2))