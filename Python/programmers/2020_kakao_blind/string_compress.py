
def check(s, k) -> int:
    start = 0
    before = ""
    total_length = len(s)
    before_same = False
    sum_counter = 1
    while start + k <= len(s):
        if before == s[start:start+k]:
            # print("SAMED", "start: ",start, "end", start+k)
            if sum_counter > 1:
                if sum_counter == 9:
                    total_length += 1
                if sum_counter == 99:
                    total_length += 1
                total_length -= k
            else:
                total_length = total_length - k + 1
            sum_counter += 1
        else:
            before = s[start:start+k]
            sum_counter = 1
        start += k
        # print("start: ", start, "end", start + k, "length", total_length)
    return total_length


def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        answer = min(answer, check(s,i))
    return answer
s = "abcabcabcabcdededededede"
s = "ababcdcdababcdcd"
s = "ababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdab"
print("len s ", len(s))
# s = "xababcdcdababcdcd"
print(solution(s))