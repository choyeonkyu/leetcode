class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M, N = len(matrix), len(matrix[0]) # 3,4
        left, right = 0, M*N-1
        while left < right-1:
            mid = (left+right)/2
            row_l, col_l = left//N, left%N
            row_r, col_r = right//N, right%N
            row_m, col_m = mid//N, mid%N
            if matrix[row_m][col_m] == target:
                return True
            elif matrix[row_m][col_m] < target:
                left = mid
            else:
                right = mid
        mid = (left+right)/2
        row_l, col_l = left//N, left%N
        row_r, col_r = right//N, right%N
        row_m, col_m = mid//N, mid%N
        if matrix[row_l][col_l] == target or matrix[row_m][col_m] == target or matrix[row_r][col_r] == target:
            return True
        else:
            return False