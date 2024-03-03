class Solution:
    def totalNQueens(self, n: int) -> int:
        self.n = n
        path = []
        start = 0
        left = set(range(n))
        self.answer = 0
        self.dfs(start, path, left)
        return self.answer

    def dfs(self, col, path, left):
        if col == self.n:
            # all queens placed, this must be a solution
            self.answer += 1

        # remember to use list(left) since we mutate left during the loop
        for row in list(left):
            if col > 0:
                # check for diagonal constraint
                valid = True
                for other_col, other_row in enumerate(path[:col]):
                    if abs(row-other_row) == abs(col-other_col):
                        valid = False
                        break

                if not valid:
                    continue
            
            # place piece and search next position
            left.remove(row)
            self.dfs(col+1, path + [row], left)
            left.add(row)
        