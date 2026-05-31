
def conv_idx(target: int, n:int ) -> tuple[int, int]:
    return target // n, target % n



class Solution:



    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n -1
        
        while l <= r:
            mid_flat = l + (r - l) // 2
            mid_row, mid_col = conv_idx( mid_flat, n)
            mid_val = matrix[mid_row][mid_col]
            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid_flat + 1
            else:
                r = mid_flat - 1
    
        return False