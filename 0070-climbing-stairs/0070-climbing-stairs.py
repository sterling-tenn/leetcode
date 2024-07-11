class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climb(n, memo)
    
    def climb(self, n, memo) -> int:
        if n in memo:
            return memo[n]
        
        if n <= 2:
            res = n
        else:
            res = self.climb(n-1, memo) + self.climb(n-2, memo)
        memo[n] = res
        return res
        