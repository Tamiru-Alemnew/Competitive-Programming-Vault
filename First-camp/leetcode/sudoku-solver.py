class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        pos = lambda i: (i>=3)+(i>=6)
        def check(b, x, y, t):
            if t in b[x]:
                return False
            
            for i in range(9):
                if t == b[i][y]:
                    return False

            x, y = pos(x)*3, pos(y)*3 
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if t == b[i][j]:
                        return False
            return True

        def bt(b, x, y):
            if x >= 9:
                for x in range(9):
                    board[x] = b[x][:]
                return

            if b[x][y].isalnum():
                if y+1 == 9:
                    bt(b, x+1, 0)
                else:
                    bt(b, x, y+1)
            else:
                for i in range(1, 10):
                    if check(b, x, y, str(i)):
                        b[x][y] = str(i)
                        if y+1 == 9:
                            bt(b, x+1, 0)
                        else:
                            bt(b, x, y+1)
                        b[x][y] = "."
                    
        bt(board[:], 0, 0)