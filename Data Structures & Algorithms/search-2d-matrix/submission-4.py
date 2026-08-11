from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        col_0 = []
        for i in range(m):
            col_0.append(matrix[i][0])
        
        row_index = bisect_left(col_0, target)
        if row_index >= m:
            row_index = m - 1
        if col_0[row_index] > target:
            row_index = row_index - 1

        if row_index < 0:
            return False

        row = matrix[row_index]

        col_index = bisect_left(row, target)
        return col_index < n and row[col_index] == target
        