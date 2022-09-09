from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force -> time limit exceed
        # result = []
        # for i in range(len(nums) - k + 1):
        #     result.append(max(nums[i:i+k]))
        # return result
        result = []
        window = collections.deque()
        for i, v in enumerate(nums):
            while window and window[-1] < v:
                window.pop()
            window.append(v)
            if i < k - 1:
                continue
            else:
                result.append(window[0])
                if nums[i - k + 1] == window[0]:
                    window.popleft()
        return result

nums = [1,3,-1,-3,5,3,6,7]
sol = Solution()
print(sol.maxSlidingWindow(nums, 3))