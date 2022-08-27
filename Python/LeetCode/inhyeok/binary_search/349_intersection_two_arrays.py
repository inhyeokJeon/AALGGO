from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))


temp = Solution()
print(temp.intersection([4,9,5], [9,4,9,8,4]))