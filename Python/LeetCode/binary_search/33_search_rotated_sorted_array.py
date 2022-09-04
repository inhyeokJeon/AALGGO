from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # find pivot
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid - 1

        pivot = left
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_pivot = (mid + pivot) % len(nums)
            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot

        return -1
        # result = bisect.bisect_left(nums, target)
        # return result


nums = [4, 5, 6, 7, 0, 1, 2] # pivot = 3
target = 0
# nums = [4,5,6,7,0,1,2]
# target = 3
sol = Solution()
print(sol.search(nums, target))
