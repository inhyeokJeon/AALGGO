import sys

N = int(sys.stdin.readline().strip())
tables = [None] * N
for _ in range(N):
    tables[_] = list(sys.stdin.readline().strip())
result = ""

def check(table):
    w_c = 0
    b_c = 0
    total = len(table) * len(table)
    for t in table:
        for temp in t:
            if temp == "1":
                b_c += 1
            else:
                w_c += 1
    if b_c == total:
        return "B"
    elif w_c == total:
        return "W"
    return 0

def solve(table):
    global result
    # check 이미 완성 되어 있는지
    ret = check(table)
    if ret == "B":
        result += "1"
        return
    elif ret == "W":
        result += "0"
        return
    div_n = len(table) // 2
    result += "("

    solve([table[i][:div_n] for i in range(div_n)])
    solve([table[i][div_n:] for i in range(div_n)])
    solve([table[i][:div_n] for i in range(div_n, div_n * 2)])
    solve([table[i][div_n:] for i in range(div_n, div_n * 2)])

    result += ")"

def main():
    solve(tables)

main()
print(result)

