import sys
import math
N = int(sys.stdin.readline().strip())
MOD = 1_000_000_007
init = [[1,1],[1,0]]

def fast_pow(b):
    # print(init)
    if b == 0:
        return [[1,0], [0,1]]
    if b == 1:
        return [[1,1],[1,0]]
    temp = fast_pow(b // 2)
    if b % 2 == 0:
        return solution(temp, temp)
    else:
        return solution(solution(temp, temp), init)

def solution(F, S):
    return [[(F[0][0] * S[0][0] % MOD + F[0][1] * S[1][0] % MOD) % MOD, (F[0][0] * S[0][1] % MOD + F[0][1] * S[1][1] % MOD) % MOD],
            [(F[1][0] * S[0][0] % MOD + F[1][1] * S[1][0] % MOD) % MOD, (F[1][0] * S[0][1] % MOD + F[1][1] * S[1][1] % MOD) % MOD]]

def solve():
    if N == 0:
        print(0)
    elif N == 1:
        print(1)
    elif N == 2:
        print(1)
    else:
        print(fast_pow(N - 1)[0][0] % MOD)

solve()