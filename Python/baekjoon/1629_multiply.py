import sys

def powpow(a, b, c):
    if b == 1:
        return a % c
    temp = powpow(a, b // 2, c)
    if b % 2 == 0: # 짝
        return temp * temp % c
    else: # 홀
        return temp * temp * a % c
def solution():
    a, b, c = list(map(int, sys.stdin.readline().strip().split()))
    if c == 1:
        print(0)
        return
    print(powpow(a,b,c))
solution()