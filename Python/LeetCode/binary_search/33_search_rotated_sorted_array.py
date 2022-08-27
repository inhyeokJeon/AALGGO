class Solution:
    def search(self, nums: List[int], target: int) -> int:
        original_index = 0
        try:
            original_index = nums.index(target)
        except ValueError:
            return -1
        return original_index


