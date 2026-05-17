class Solution:
    def dfsMatrix(self, r, c, grid, visited):
        rows = len(grid)
        cols = len(grid[0])
        if r >= rows or c >= cols or min(r,c) < 0 or (r,c) in visited or grid[r][c] == 1:
            return 0
        if r == rows - 1 and c == cols - 1:
            return 1
        
        if grid[r][c] == 0:
            visited.add((r, c))

        count = 0
        count += self.dfsMatrix(r+1, c, grid, visited)
        count += self.dfsMatrix(r, c+1, grid, visited)
        count += self.dfsMatrix(r-1, c, grid, visited)
        count += self.dfsMatrix(r, c-1, grid, visited)

        visited.remove((r, c))  # ✅ nécessaire pour permettre d'autres chemins

        return count
        return count


    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        return self.dfsMatrix(0,0, grid, visited)

