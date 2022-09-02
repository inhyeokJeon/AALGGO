from typing import *
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 1, 2
        red_counter, white_counter, blue_counter = nums.count(red), nums.count(white) + nums.count(red), len(nums)
        for i in range(len(nums)):
            if i < red_counter:
                nums[i] = red
                continue
            elif i < white_counter:
                nums[i] = white
                continue
            nums[i] = blue

    def sortColors(self, nums: List[int]) -> None:
        """
        퀵정렬로 바꾸자.
        -> 더오래 걸림. 순회하기 떄문에
        """
        red, white, blue = 0, 0, len(nums)
        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1
        print(nums)

nums = [2,0,2,1,1,0]
# nums = [2,0,1]
sol = Solution()
sol.sortColors(nums)