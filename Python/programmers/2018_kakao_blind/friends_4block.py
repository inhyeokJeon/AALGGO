def solution(m, n, board):
    board_list = [list(i) for i in board]

    def check(i, j):
        if board_list[i][j] == board_list[i + 1][j] == board_list[i][j + 1] == board_list[i + 1][j + 1] != '#':
            return True
        return False

    def char_to_sharp(i,j):
        board_list[i][j] = board_list[i + 1][j] = board_list[i][j + 1] = board_list[i + 1][j + 1] = "#"

    matched = True
    while matched:
        matched = []
        # 4개가 똑같은 것 좌표를 matched 에 저장.
        for i in range(m-1):
            for j in range(n-1):
                if check(i, j):
                    matched.append([i,j])
        # matched 에 저장된 값들 # 으로 삭제
        for i, j in matched:
            char_to_sharp(i,j)
        # "#"인 값들 밑으로 내리기
        count = 0
        while count < m:
            for j in range(n):
                for i in range(m - 1):
                    if board_list[i][j] != "#" and board_list[i + 1][j] == "#":
                        board_list[i][j], board_list[i + 1][j] = board_list[i + 1][j], board_list[i][j]
            count += 1
        # matched 에 저장된 값들 #으로 바꾸기
    return sum([row.count("#") for row in board_list])

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m,n,board))