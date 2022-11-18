import sys

def main():
    n = int(sys.stdin.readline().strip())
    answer = []
    answer_count = n + 1
    def brute(num, count, temp):
        nonlocal answer
        nonlocal answer_count
        if answer_count <= count:
            return
        if num == 1:
            answer = temp + [1]
            answer_count = count
            return
        if num % 3 == 0:
            brute(num // 3, count + 1, temp + [num])
        if num % 2 == 0:
            brute(num // 2, count + 1, temp + [num])
        brute(num - 1, count + 1, temp + [num])

    brute(n, 0, [])
    print(answer_count)
    print(*answer)
if __name__ == "__main__":
    main()
