import sys

def main():
    n = int(sys.stdin.readline().strip())

    def get_prime_list(num):
        temp = [False, False] + [True] * num
        for i in range(2, int(num ** 0.5) + 1):
            if temp[i]:
                for j in range(i * i, num, i):
                    temp[j] = False
        return [i for i in range(2, num) if temp[i]]
    numbers = [0] + get_prime_list(n + 1)
    # print(numbers)
    for i in range(1, len(numbers)):
        numbers[i] = numbers[i] + numbers[i-1]
    start = 0
    end = 1
    answer = 0
    # print(numbers)
    while start < end and end < (len(numbers)):
        # 방향은 start, end 둘중 작은 놈이 움직인다.(한명만)
        if numbers[end] - numbers[start] > n:
            start += 1
        elif numbers[end] - numbers[start] < n:
            end += 1
        else:  # 같으면
            start += 1
            answer += 1

    print(answer)
if __name__ == "__main__":
    main()
