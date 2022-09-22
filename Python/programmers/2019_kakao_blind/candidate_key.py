import itertools

def solution(relation):
    answer = []
    col_relation = []
    unique = []
    row_length = len(relation)
    col_length = len(relation[0])
    candidate = [_ for _ in range(col_length)]
    for times in range(1, col_length + 1):
        for perm in itertools.combinations(candidate, times):
            temp = set()
            for row in range(row_length):
                string = ""
                for p in perm:
                    string += relation[row][p]
                temp.add(string)
            if len(temp) == row_length:
                unique.append(set(perm))

    while unique:
        good = unique.pop(0)
        answer.append(good)
        will_remove = []
        for idx, uniq in enumerate(unique):
            if good.difference(uniq):
                continue
            else:
                will_remove.append(idx)

        for idx in reversed(will_remove):
            unique.pop(idx)

    return len(answer)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))