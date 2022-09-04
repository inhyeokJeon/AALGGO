from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return -1

numbers = [2,7,9,11]
target = 9
temp = Solution()
print(temp.twoSum(numbers, target))