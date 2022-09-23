def solution(new_id: str) -> str:
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = [ _ for _ in new_id.lower()]
    # print(new_id)
    will_be_removed = []
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    for idx, char in enumerate(new_id):
        if char not in "0123456789abcdefghijklmnopqrstuvwxyz-_.":
            will_be_removed.append(idx)
    for idx in reversed(will_be_removed):
        new_id.pop(idx)
    # print(new_id)
    position = 0
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while position + 1< len(new_id):
        if new_id[position + 1] == new_id[position] == ".":
            new_id.pop(position)
        else:
            position += 1
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    count = 2
    # print(new_id)
    while new_id and count > 0:
        if new_id[0] == ".":
            new_id.pop(0)
        elif new_id[-1] == ".":
            new_id.pop()
        count -= 1
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(new_id) == 0:
        new_id = ["a"]
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id.pop()
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(new_id) <= 2:
        new_id.append(new_id[-1])
    # print(new_id)
    answer = ''.join(new_id)
    return answer

new_ids = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]
for new_id in new_ids:
    print(solution(new_id))