# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        memo = defaultdict(int)

        def dfs(row: int, col: int) -> int:
            if memo[(row, col)] != 0:
                return memo[(row, col)]

            max_path_length = 1
            for d_row, d_col in directions:
                new_row, new_col = row + d_row, col + d_col
                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                    max_path_length = max(max_path_length, 1 + dfs(new_row, new_col))

            memo[(row, col)] = max_path_length
            return max_path_length

        max_path = 0
        for i in range(rows):
            for j in range(cols):
                max_path = max(max_path, dfs(i, j))

        return max_path