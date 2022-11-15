import sys

def main():
    n = int(sys.stdin.readline().strip())
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    x = int(sys.stdin.readline().strip())
    answer = 0
    numbers.sort()
    start = 0
    end = n - 1
    while start < end:
        if numbers[start] + numbers[end] < x:
            start += 1
        elif numbers[start] + numbers[end] > x:
            end -= 1
        else:
            start += 1
            end -= 1
            answer += 1

    print(answer)

if __name__ == "__main__":
    main()
