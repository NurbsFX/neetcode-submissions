class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [set() for _ in range(9)]

        n = len(board)

        for i in range(n):
            currentLine = set()
            for j in range(n):
                value = board[i][j]
                if value == '.':
                    continue
                elif value not in currentLine:
                    currentLine.add(value)
                else:
                    return False

        for j in range(n):
            currentColumn = set()
            for i in range(n):
                value = board[i][j]
                if value == '.':
                    continue
                elif value not in currentColumn: 
                    currentColumn.add(value)
                else: 
                    return False

        for i in range(n):
            for j in range(n):
                lineSquare, columnSquare = i // 3, j // 3
                value = board[i][j]
                if value == '.':
                    continue 
                elif value not in squares[lineSquare * 3 + columnSquare]:
                    squares[lineSquare * 3 + columnSquare].add(value)
                else:
                    return False

        return True


        