class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        seen = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= columns or (i,j) in seen: 
                return
            seen.add((i,j))
            if grid[i][j] == "1":
                grid[i][j] = 0
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)
        
        count = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        
        return count
            
            

            