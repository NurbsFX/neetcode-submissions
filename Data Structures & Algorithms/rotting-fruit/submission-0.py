class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])

        visited = set()
        queue = deque()

        minute = 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    visited.add((i,j))
                    queue.append((i,j))  

        while queue: 
            for _ in range(len(queue)):
                r, c = queue.popleft()

                neighbours = [[0, 1], [1, 0], [-1, 0], [0, -1]] 
                for dr, dc in neighbours:
                    if min(r + dr, c + dc) < 0 or (r + dr, c + dc) in visited or r + dr == rows or c + dc == columns or grid[r +dr][c + dc] != 1:
                        continue
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
                    grid[r + dr][c + dc] = 2
            if queue:
                minute += 1

        for row in grid:
            if 1 in row:
                return -1
        
        return minute