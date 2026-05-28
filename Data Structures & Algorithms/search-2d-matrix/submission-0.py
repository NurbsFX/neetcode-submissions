class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        goodRaw = -1

        # first, we look for the good row
        firstRow, lastRow = 0, n - 1

        while firstRow <= lastRow and goodRaw == -1:
            middleRow = (firstRow + lastRow)//2
            
            if target <= matrix[middleRow][m-1] and target >= matrix[middleRow][0]:
                goodRaw = middleRow
                break
            elif target > matrix[middleRow][m-1]:
                firstRow = middleRow + 1
            else:
                lastRow = middleRow - 1

        # now, we look for the good column

        if goodRaw != -1:
            firstColumn, lastColumn = 0, m - 1
            while firstColumn <= lastColumn:
                middleColumn = (firstColumn + lastColumn)//2
                if target == matrix[goodRaw][middleColumn]:
                    return True
                elif target < matrix[goodRaw][middleColumn]:
                    lastColumn = middleColumn - 1
                else:
                    firstColumn = middleColumn + 1
        
        return False