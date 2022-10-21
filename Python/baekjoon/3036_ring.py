import sys
import math
N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))

first = numbers.pop(0)
for number in numbers:
    gcd = math.gcd(first, number)
    print(f"{first // gcd}/{number // gcd}")
