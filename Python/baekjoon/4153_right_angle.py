import sys
import math

def solve():
    while True:
        first, second, third = list(map(int, sys.stdin.readline().strip().split()))
        if first == second == third == 0:
            break

        if first < second and second < third: # third
            if math.pow(third, 2) == (math.pow(first, 2) + math.pow(second, 2)):
                print("right")
                continue
        elif first < second and third < second:
            if math.pow(second, 2) == (math.pow(first, 2) + math.pow(third, 2)):
                print("right")
                continue
        else: # first 비거
            if math.pow(first, 2) == (math.pow(third, 2) + math.pow(second, 2)):
                print("right")
                continue
        print("wrong")
solve()