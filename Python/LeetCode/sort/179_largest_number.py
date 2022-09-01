from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def need_change(num1, num2) -> bool:
            """
            바꿔야된다면
            """
            if len(num1) == len(num2):
                return num1 < num2
            num1_first = num1 + num2
            num2_first = num2 + num1
            return int(num1_first) < int(num2_first)

        if len(nums) == 1:
            return str(nums[0])
        done = [nums[0]]
        ready = nums[1:]
        position = 1
        while ready:
            done.append(ready.pop(0))
            for i in range(len(done)-1, 0, -1):
                if need_change(str(done[i-1]), str(done[i])):
                    done[i-1], done[i] = done[i], done[i-1]
                else:
                    break
            position += 1
        result = ""
        for d in done:
            result += str(d)
        result = int(result)
        return str(result)

sol = Solution()
print(sol.largestNumber([111311, 1113]))
print(sol.largestNumber([3,30,34,5,9]))
print(sol.largestNumber([34323,3432]))
print(sol.largestNumber([0,0]))