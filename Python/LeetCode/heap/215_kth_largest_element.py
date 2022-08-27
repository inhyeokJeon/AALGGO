import heapq

# heapq 이용
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        hq = []
        for num in nums:
            heapq.heappush(hq, -num) # maxheap 만들기 위해서
        for _ in range(k - 1):
            heapq.heappop(hq)
        return -heapq.heappop(hq)

# 정렬 방법
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]