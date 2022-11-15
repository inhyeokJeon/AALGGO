import sys

def main():
    n = int(sys.stdin.readline().strip())
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    answer = 2_000_000_000
    numbers.sort()
    start = 0
    end = n - 1
    answer_first, answer_second = -1_000_000_000, 1_000_000_000
    while start < end:
        two_sum = numbers[start] + numbers[end]
        abs_two_sum = abs(two_sum)
        if abs_two_sum < answer:
            answer_first = numbers[start]
            answer_second = numbers[end]
            answer = abs_two_sum
            if answer == 0:
                print(answer_first, answer_second)
                return
        if two_sum < 0:
            start += 1
        elif two_sum > 0:
            end -= 1

    print(answer_first, answer_second)

if __name__ == "__main__":
    main()
