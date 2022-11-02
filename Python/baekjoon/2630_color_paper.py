import sys

N = int(sys.stdin.readline().strip())
tables = [None] * N
for _ in range(N):
    tables[_] = list(map(int, sys.stdin.readline().strip().split()))
white = 0
black = 0
def partition(partition):
    global white, black
    white_count = 0
    black_count = 0
    div_n = len(partition)
    for temp in partition:
        white_count += temp.count(0)
        black_count += temp.count(1)

    if white_count == div_n * div_n:
        white += 1
        # print("white score partition", partition, div_n)
        return False
    elif black_count == div_n * div_n:
        black += 1
        # print("black score partition", partition, div_n)
        return False
    return True

def check(table):
    global white, black
    w_c = 0
    b_c = 0
    total = len(table) * len(table)
    for t in table:
        for temp in t:
            if temp == 1:
                b_c += 1
            else:
                w_c += 1
    if b_c == total:
        black += 1
        return True
    elif w_c == total:
        white += 1
        return True
    return False

def solve(table, div_n):
    global white, black
    # print(table, div_n)
    # check 이미 완성 되어 있는지
    if check(table):
        return
    left_upper = partition([table[i][:div_n] for i in range(div_n)])
    right_upper = partition([table[i][div_n:] for i in range(div_n)])
    left_lower = partition([table[i][:div_n] for i in range(div_n, div_n * 2)])
    right_lower = partition([table[i][div_n:] for i in range(div_n, div_n * 2)])
    if not left_upper and not right_upper and not left_lower and not right_lower:
        return
    else:
        if left_upper:
            solve([table[i][:div_n] for i in range(div_n)], div_n // 2)
        if right_upper:
            solve([table[i][div_n:] for i in range(div_n)], div_n // 2)
        if left_lower:
            solve([table[i][:div_n] for i in range(div_n, div_n * 2)], div_n // 2)
        if right_lower:
            solve([table[i][div_n:] for i in range(div_n, div_n * 2)], div_n // 2)

solve(tables, N // 2)

print(white)
print(black)


