import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        print(index)
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

#         if len(nums) == 1:
#             if nums[0] == target:
#                 return 0

#         def bst(left, right):
#             if left <= right:
#                 mid = (left + right) // 2
#                 if nums[mid] < target:
#                     return bst(mid + 1, right)
#                 elif nums[mid] > target:
#                     return bst(left, mid - 1)
#                 else:
#                     return mid
#             else:
#                 return -1


#         return bst(0, len(nums) - 1)