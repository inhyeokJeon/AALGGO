import sys
import math
number= int(sys.stdin.readline().strip())
fac = str(math.factorial(number))
ret = 0
for i in range(len(fac) -1, -1, -1):
    if fac[i] == '0':
        ret += 1
    else:
        break
print(ret)