def convert(n, k) -> str:
    q, r = divmod(n, k)
    if q == 0:
        return str(r)
    else:
        return convert(q, k) + str(r)

def primenumber(n):
    if n <= 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def solution(n, k):
    changed = convert(n, k)
    arr = changed.split('0')  # 0을 기준으로 나눠줌
    answer = 0
    for num in arr:
        if num and primenumber(int(num)):
            answer += 1
    return answer

n = 437674
k = 3
print(solution(n,k))