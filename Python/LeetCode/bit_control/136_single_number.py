# 모두 XOR 하면 중복되지 않은 값만 남는다.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num
        return result