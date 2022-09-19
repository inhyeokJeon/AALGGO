from typing import List
import heapq


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        candidates = [1] * len(gas)
        now = 0
        for idx in range(len(gas)):
            gas_cost = gas[idx] - cost[idx]

            if total + gas_cost < 0:
                # print("idx", idx, "now: ", now)
                # for i in range(now, idx + 1):
                #     candidates[i] = 0
                now = idx + 1
                total = 0
            else:
                total += gas_cost
        #         print("idx", idx, "total : ", total)
        # print(candidates)
        return now

gas =  [5,8,2,8] # [3,1,1] # [1,2,3,4,5] # [5,1,2,3,4] #

cost = [6,5,6,6] # [1,2,2] # [3,4,5,1,2] # [4,4,1,5,1] #
sol = Solution()

print(sol.canCompleteCircuit(gas, cost))