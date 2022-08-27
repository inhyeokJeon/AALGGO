# skill -> [type, r1, c1, r2, c2, degree]
# type 1 공격, 2 힐
# r -> y축, c -> x축
# degree 정도
def solution(board, skill):
    answer = 0
    y_size = len(board)
    x_size = len(board[0])
    length = len(skill)
    matrix = [[0 for _ in range(x_size + 1)] for _ in range(y_size + 1)]
    for ski in skill:
        type, r1, c1, r2, c2, degree = ski
        if type == 1:
            matrix[r1][c1] -= degree
            matrix[r1][c2 + 1] += degree
            matrix[r2 + 1][c1] += degree
            matrix[r2 + 1][c2 + 1] -= degree
        elif type == 2:
            matrix[r1][c1] += degree
            matrix[r1][c2 + 1] -= degree
            matrix[r2 + 1][c1] -= degree
            matrix[r2 + 1][c2 + 1] += degree

    # 오른쪽 방향
    for y in range(y_size):
        for x in range(x_size):
            matrix[y][x + 1] += matrix[y][x]

    for x in range(x_size):
        for y in range(y_size):
            matrix[y + 1][x] += matrix[y][x]

    for i in range(y_size):
        for j in range(x_size):
            board[i][j] += matrix[i][j]
            if board[i][j] > 0:
                answer += 1

    # 왼쪽 방향
    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))