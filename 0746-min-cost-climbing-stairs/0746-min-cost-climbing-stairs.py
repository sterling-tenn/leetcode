class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def get_cost(i):
            if i in memo:
                return memo[i]
            
            if i == 0 or i == 1:
                memo[i] = cost[i]
            else:
                memo[i] = cost[i] + min(get_cost(i-1), get_cost(i-2))
            return memo[i]
        
        n = len(cost)
        return min(get_cost(n-1), get_cost(n-2))