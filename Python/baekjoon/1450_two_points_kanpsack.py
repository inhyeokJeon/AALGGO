import sys
import bisect

def main():
    answer = 0
    n, c = list(map(int, sys.stdin.readline().strip().split()))
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    if n == 1:
        if numbers[0] <= c:
            print(2)
            return
        else:
            print(1)
            return
    a = numbers[:len(numbers) // 2]
    b = numbers[len(numbers) // 2:]
    def brute_force(index, num, length, temp_list, check):
        if index == length:
            temp_list.append(num)
            return
        brute_force(index + 1, num, length, temp_list, check)  # 안넣었을 때
        if check == 0:
            brute_force(index + 1, num + a[index], length, temp_list, check) # 넣었을 때
        if check == 1:
            brute_force(index + 1, num + b[index], length, temp_list, check) # 넣었을 때


    a_list, b_list = [], []
    brute_force(0, 0, len(a), a_list, 0)
    brute_force(0, 0, len(b), b_list, 1)
    b_list.sort()
    for value in a_list:
        if value > c:
            continue
        answer += bisect.bisect_right(b_list, c - value)
    print(answer)


if __name__ == "__main__":
    main()
