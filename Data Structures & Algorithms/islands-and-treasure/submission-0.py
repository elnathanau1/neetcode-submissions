from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j,0))
                    seen.add((i,j))
        
        while queue:
            i,j,distance = queue.popleft()
            for a,b in [(i+1, j), (i-1, j), (i,j-1), (i,j+1)]:
                if a >= 0 and a < m and b >= 0 and b < n and (a,b) not in seen and grid[a][b] > 0:
                    grid[a][b] = distance + 1
                    seen.add((a,b))
                    queue.append((a,b,distance + 1))
        
