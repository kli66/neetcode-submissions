class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m, n = len(matrix), len(matrix[0])

        zero_cols = set()
        zero_rows = set()
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in range(m):
            for c in range(n):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0
                    