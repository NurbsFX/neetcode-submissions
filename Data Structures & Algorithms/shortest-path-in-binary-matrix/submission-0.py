class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def bfs(grid):
            rows, columns = len(grid), len(grid[0])

            if grid[0][0] == 1 or grid[rows - 1][columns - 1] == 1:
                return -1

            visited = set()
            queue = deque()

            visited.add((0, 0))
            queue.append((0, 0))
            length = 1
            
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    if r == rows - 1 and c == columns - 1:
                        return length
                    
                    neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

                    for dr, dc in neighbours:
                        nr, nc = r + dr, c + dc

                        if nr < 0 or nc < 0 or nr == rows or nc == columns:
                            continue

                        if grid[nr][nc] == 1 or (nr, nc) in visited:
                            continue

                        queue.append((nr, nc))
                        visited.add((nr, nc))

                length += 1

            return -1

        return bfs(grid)