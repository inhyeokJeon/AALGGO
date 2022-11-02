import sys
# 페르마 소정리
# a^(p-1) = 1 (p 가 소수일 떄) a 를 k!(n-k)! 로 잡음 => (k!(n-k)!) ^ (p-1) = 1
# nCr = (n! / (k!(n-k)!)) * 1
# nCr = (n! / (k!(n-k)!)) * (k!(n-k)!) ^ (p-1)
# nCr = (n! * (k!(n-k)!)^(p-2)) % p
# nCr = (n! % p * k! ^ (p-2) % p (n-k)!^(p-2) % mod) % p
a, b = list(map(int, sys.stdin.readline().strip().split()))
MOD = 1_000_000_007
def factorial(n):
    if n == 0:
        return 1
    for i in range(n-1, 1, -1):
        n = n * i % MOD
    return n
def fast_pow(a, b):
    if b == 1:
        return a % MOD
    temp = fast_pow(a, b // 2)
    if b % 2 == 0:
        return temp * temp % MOD
    else:
        return temp * temp * a % MOD

A = factorial(a) % MOD
B = fast_pow(factorial(b) % MOD, MOD - 2) % MOD
C = fast_pow(factorial(a-b) % MOD, MOD - 2) % MOD
print(A * B * C % MOD)