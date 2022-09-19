from typing import List
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        # result = float("-inf")
        for i in range(1, len(nums)):
            dp.append(nums[i] + (dp[i-1] if dp[i-1] > 0 else 0))

        return max(dp)
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] # [5,4,-1,7,8]
sol = Solution()
print(sol.maxSubArray(nums))
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.