
                if in_bound(new_row , new_col) and grid[new_row][new_col] == 1:
                    if not visited[new_row][new_col]:
                        dfs(new_row , new_col)

                    possible -=1  

            perimeter += possible

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    dfs(i , j)
                    return perimeter

[
