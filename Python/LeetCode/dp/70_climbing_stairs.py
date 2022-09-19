"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2, 3]
        if n < 4:
            return dp[n]
        for i in range(4, n + 1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[i]

sol = Solution()
print(sol.climbStairs(4))