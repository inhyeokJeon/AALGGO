import sys
N = int(sys.stdin.readline().strip())

fib1_count = 0
fib2_count = 0
def fib1(n):
    global fib1_count
    if n == 1 or n == 2:
        fib1_count += 1
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    global fib2_count
    f = [0] * (N)
    f[0] = f[1] = 1
    for i in range(2, n):
        fib2_count += 1
        f[i] = f[i-1] + f[i-2]
    return f[n - 1]

fib1(N)
fib2(N)
print(fib1_count)
print(fib2_count)