from typing import *


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def sort_algorithm(l1, l2) -> bool:
            return l1[0]**2 + l1[1]**2 < l2[0]**2 + l2[1]**2

        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        return points[:k]


# points = [[1,3],[-2,2]]
points = [[3,3],[5,-1],[-2,4]]
sol = Solution()
print(sol.kClosest(points, 2))