from typing import List

"""
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 10**4.
"""


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def dfs(s):
            result = []
            for idx, char in enumerate(s):
                if char in "+-*":
                    left = dfs(s[:idx])
                    right = dfs(s[idx+1:])
                    for l in left:
                        for r in right:
                            if char == "+":
                                result.append(l + r)
                            elif char == "-":
                                result.append(l - r)
                            elif char == "*":
                                result.append(l * r)
            if not result:
                result.append(int(s))
            return result

        return dfs(expression)


expression = "2*3-4*5" # "2-1-1"
sol = Solution()
print(sol.diffWaysToCompute(expression))