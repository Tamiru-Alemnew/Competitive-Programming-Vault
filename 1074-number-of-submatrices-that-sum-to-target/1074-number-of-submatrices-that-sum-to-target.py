class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ps = [[0]*len(matrix[0]) for i in range(len(matrix))]

        for i in range(len(matrix)):
            r = 0
            for j in range(len(matrix[0])):
                r += matrix[i][j]
                ps[i][j] += r

        for j in range(len(matrix[0])):
            for i in range(1,len(matrix)):
                ps[i][j] += ps[i-1][j]

        for p in ps:
            print(p)

        ans = 0
        for r1 in range(len(ps)):
            for r2 in range(r1,len(ps)):
                ps_count = defaultdict(int)
                ps_count[0] = 1
                for c in range(len(ps[0])):
                    cur_sum = ps[r2][c] - ( ps[r1-1][c] if r1 > 0  else 0 )
                    diff = cur_sum - target
                    ans += ps_count[diff]
                    ps_count[cur_sum] +=1

        return ans