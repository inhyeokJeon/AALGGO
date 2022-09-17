from typing import List
import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        hq = []
        for person in people:
            heapq.heappush(hq, (-person[0], person[1]))
        result = []
        while hq:
            person = heapq.heappop(hq)
            result.insert(person[1], (-person[0], person[1]))
        return result
        # return people

peoples = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# sol = [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
sol = Solution()
print(sol.reconstructQueue(peoples))