import sys

def main():
    n, s = list(map(int, sys.stdin.readline().strip().split()))
    numbers = [0] + list(map(int, sys.stdin.readline().strip().split()))
    for i in range(1, n + 1):
        numbers[i] = numbers[i-1] + numbers[i]

    start = 0
    end = 1
    min_length = float("inf")
    while start < end and end < (n + 1):
        # 방향은 start, end 둘중 작은 놈이 움직인다.(한명만)
        if numbers[end] - numbers[start] >= s:
            min_length = min(min_length, end - start)
            start += 1
        else:
            end += 1
    if min_length == float("inf"):
        print(0)
    else:
        print(min_length)

if __name__ == "__main__":
    main()
