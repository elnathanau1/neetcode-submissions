from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        seen = set()
        def countIsland(i, j):
            count = 1
            queue = deque()
            queue.append((i,j))
            seen.add((i,j))

            while queue:
                i,j = queue.popleft()
                for a,b in [(i+1,j), (i-1,j), (i,j-1), (i,j+1)]:
                    if (a,b) not in seen and a >= 0 and b >= 0 and a < len(grid) and b < len(grid[0]) and grid[a][b] == 1:
                        seen.add((a,b))
                        queue.append((a,b))
                        count += 1

            nonlocal max_area
            max_area = max(count, max_area)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in seen:
                    countIsland(i,j)

        
        return max_area