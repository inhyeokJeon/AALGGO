from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force -> time limit exceed
        result = []
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i:i+k]))
        return result
        # for i, v in enumerate(nums):

nums = [1,3,-1,-3,5,3,6,7]
sol = Solution(),
print(sol.maxSlidingWindow(nums, 3))