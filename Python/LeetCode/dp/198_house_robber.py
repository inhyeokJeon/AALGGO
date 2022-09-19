from typing import List
from collections import defaultdict
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        nums.insert(0, 0)
        if len(nums) <= 2:
            return max(nums)
        for i in range(3, length + 1):
            nums[i] = max(nums[i-3], nums[i-2]) + nums[i]

        return max(nums[length], nums[length - 1])

nums = [2,7,9,3,1]
sol = Solution()
print(sol.rob(nums))
"""Example
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""