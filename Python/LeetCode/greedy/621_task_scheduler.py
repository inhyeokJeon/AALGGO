from typing import List
import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        result = 0
        while True:
            count = 0
            for task, _ in counter.most_common(n+1):
                if counter[task] >= 1:
                    counter[task] -= 1
                    count += 1
                    result += 1
            if counter.most_common()[0][1] <= 0:
                break

            result += n + 1 - count
        return result
tasks = ["A","A","A","B","B","B"]
# tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
# sol = 16
sol = Solution()
print(sol.leastInterval(tasks, n))