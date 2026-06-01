class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, columns = len(image), len(image[0])
        
        originColor = image[sr][sc]
        if originColor == color:
            return image

        visit = set((sr, sc))
        def dfs(r, c, visit):
            if min(r, c) < 0 or r == rows or c == columns or (r, c) in visit or image[r][c] != originColor:
                return
            
            if image[r][c] == originColor:
                visit.add((r, c))
                image[r][c] = color
                dfs(r + 1, c, visit)
                dfs(r - 1, c, visit)
                dfs(r, c + 1, visit)
                dfs(r, c - 1, visit)
                visit.remove((r, c))

        dfs(sr, sc, visit)
        return image