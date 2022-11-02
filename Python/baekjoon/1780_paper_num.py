import sys

N = int(sys.stdin.readline().strip())
tables = [None] * N
for _ in range(N):
    tables[_] = list(map(int, sys.stdin.readline().strip().split()))
zero_count = 0
one_count = 0
minus_count = 0


def check(table):
    one_c = 0
    zero_c = 0
    minus_c = 0
    total = len(table) * len(table)
    for t in table:
        for temp in t:
            if temp == 1:
                one_c += 1
            elif temp == 0:
                zero_c += 1
            else:
                minus_c += 1
    if one_c == total:
        return "O"
    elif zero_c == total:
        return "Z"
    elif minus_c == total:
        return "M"
    return 0

def solve(table):
    global one_count, zero_count, minus_count
    # print(table, div_n)
    # check 이미 완성 되어 있는지
    ret = check(table)
    if ret == "O":
        one_count += 1
        return
    elif ret == "Z":
        zero_count += 1
        return
    elif ret == "M":
        minus_count += 1
        return
    div_n = len(table) // 3
    # 위 세개
    solve([table[i][:div_n] for i in range(div_n)])
    solve([table[i][div_n:div_n * 2] for i in range(div_n)])
    solve([table[i][div_n * 2:] for i in range(div_n)])

    solve([table[i][:div_n] for i in range(div_n, div_n * 2)])
    solve([table[i][div_n:div_n * 2] for i in range(div_n, div_n * 2)])
    solve([table[i][div_n * 2:] for i in range(div_n, div_n * 2)])

    solve([table[i][:div_n] for i in range(div_n * 2, len(table))])
    solve([table[i][div_n:div_n * 2] for i in range(div_n * 2, len(table))])
    solve([table[i][div_n * 2:] for i in range(div_n * 2, len(table))])


def main():
    solve(tables)
    print(minus_count)
    print(zero_count)
    print(one_count)
main()


