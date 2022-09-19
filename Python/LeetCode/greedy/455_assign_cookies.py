from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        g_index = 0
        for idx in range(max(len(s), len(g))):
            if g_index == len(g) or idx == len(s):
                break
            if s[idx] >= g[g_index]:
                g_index += 1
                result += 1
        return result


g = [1,2,3]
s = [1,1]

sol = Solution()
print(sol.findContentChildren(g, s))