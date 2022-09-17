from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        yesterday = prices[0]
        for idx in range(1, len(prices)):
            if yesterday < prices[idx]:
                result += prices[idx] - yesterday
            yesterday = prices[idx]
        return result


price = [1,2,3,4,5]
sol = Solution()
print(sol.maxProfit(price))