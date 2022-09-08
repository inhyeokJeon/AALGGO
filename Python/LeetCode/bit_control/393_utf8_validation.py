from typing import *


class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        def check(size) -> bool:
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            binary = data[start]
            if (binary >> 7) == 0:
                start += 1
            elif (binary >> 3) == 0b11110 and check(3):
                start += 4
            elif (binary >> 4) == 0b1110 and check(2):
                start += 3
            elif (binary >> 5) == 0b110 and check(1):
                start += 2
            else:
                return False
        return True

# datas = [235,140,4]
datas = [127,127,127]
sol = Solution()
print(sol.validUtf8(datas))

