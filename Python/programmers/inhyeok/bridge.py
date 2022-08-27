from collections import defaultdict


def check(ll, num, k):
    changed_list = [i - num + 1 for i in ll] + [1]
    count = 1
    print(num, changed_list)
    for i in range(len(changed_list)):
        if count > k:
            return False
        if changed_list[i] <= 0:  # 밟을 수 없는 땅.
            count += 1
        else:
            count = 1
    return True


def solution(stones, k):
    answer = 0
    length = len(stones)
    if length == 1:
        return stones[0]
    left, right = 0, length - 1
    last_left, last_right = -1, -1
    for _ in range(100):
        mid = (left + right) // 2

        print("left:", left, "right: ", right, "mid", mid)
        if check(stones, mid, k):
            left = mid
            # last_left = left
        else:
            right = mid
        # last_right = right

    answer = mid
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 4))
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))