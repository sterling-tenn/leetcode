class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = [] # rotting fruits
        n_fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    n_fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        t = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # bfs
        while queue and n_fresh > 0:
            for i in range(len(queue)):
                row, col = queue.pop(0)
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    
                    if r in range(len(grid)) and \
                    c in range(len(grid[0])) and \
                    grid[r][c] == 1:
                        queue.append((r,c))
                        grid[r][c] = 2
                        n_fresh -= 1
            t += 1
        return t if n_fresh == 0 else -1