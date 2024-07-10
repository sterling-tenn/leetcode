class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(n_open, n_closed):
            if n == n_open == n_closed:
                res.append("".join(stack))
                return
            
            if n_open < n:
                stack.append("(")
                dfs(n_open + 1, n_closed)
                stack.pop()
            if n_closed < n_open:
                stack.append(")")
                dfs(n_open, n_closed + 1)
                stack.pop()
        
            
        dfs(0, 0)
        return res