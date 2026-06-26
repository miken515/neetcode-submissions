class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        # helper function
        def addDist(r, c):
            #base cases
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == -1 or
                (r, c) in visited
            ):
                return
            q.append([r, c])
            visited.add((r, c))

        # adding treasure to visited
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                addDist(r + 1, c)
                addDist(r - 1, c)
                addDist(r, c + 1)
                addDist(r, c - 1)
            distance += 1
