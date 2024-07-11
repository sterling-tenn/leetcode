class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 0
        visited = set() # (row, col) coordinates
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(row, col) -> None:
            if row not in range(len(grid)) or \
            col not in range(len(grid[0])) or \
            grid[row][col] == "0" or \
            (row, col) in visited:
                return
            
            visited.add((row, col))
            for dr, dc in directions:
                dfs(row + dr, col + dc)
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    n_islands += 1
                    
                    
        return n_islands