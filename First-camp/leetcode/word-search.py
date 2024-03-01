class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        m, n = len(board[0]), len(board)
        dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def backtracking(c, r, cnt, visited):
            if cnt == len(word):
                nonlocal ans
                ans = True
                return

            for x, y in dir:
                new_c, new_r = c + x, r + y
                if (new_c < 0 or new_c >= n) or (new_r < 0 or new_r >= m):
                    continue
                if board[new_c][new_r] == word[cnt] and [new_c, new_r] not in visited:
                    backtracking(new_c, new_r, cnt + 1, visited + [[new_c, new_r]])

        for c in range(n):
            for r in range(m):
                if ans == False and board[c][r] == word[0]:
                    backtracking(c, r, 1, [[c, r]])
        return ans