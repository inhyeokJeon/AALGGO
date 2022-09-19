class Solution:
    def fib(self, n: int) -> int:
        fb = [0, 1]
        if n < 2:
            return fb[n]
        for i in range(2, n + 1):
            fb.append(fb[i-1] + fb[i-2])
        return fb[n]



sol = Solution()
print(sol.fib(3))