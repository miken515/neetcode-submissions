class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for directRow, directCol in directions:
                    nextrow = directRow + row
                    nextcol = directCol + col

                    if (nextrow < 0 or nextcol < 0 or nextrow >= ROWS or
                        nextcol >= COLS or grid[nextrow][nextcol] == "0"
                    ):
                        continue

                    q.append((nextrow, nextcol))
                    grid[nextrow][nextcol] = "0"
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":

                    bfs(r, c)
                    islands += 1
        
        return islands