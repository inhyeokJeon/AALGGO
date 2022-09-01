from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if result and result[-1][-1] >= interval[0]:
                result[-1][-1] = max(result[-1][-1], interval[1])
            else:
                result.append(interval)
        return result

sol = Solution()
# print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[1,4],[2,3]]))