class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        import numpy as np
        nums = np.array(matrix)
        # print(help(nums))# a.compress(condition, axis=None, out=None), a.flatten(order='C',FAK)
        nums = nums.flatten()
        left, right = 0, len(nums)-1
        if nums[left] > target or target > nums[right]:
            return False
        while left < right and right - left > 1:
            mid = (left + right)/2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        if target in nums[left:right+1]:
            return True
        else:
            return False