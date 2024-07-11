class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set() # (row, col)
        
        def dfs(row, col) -> None:
            if row not in range(len(grid)) or \
            col not in range(len(grid[0])) or \
            grid[row][col] == 0 or \
            (row, col) in visited:
                return 0
            
            visited.add((row, col))
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
        
        maxA = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == 1:
                    maxA = max(maxA, dfs(row, col))
        return maxA