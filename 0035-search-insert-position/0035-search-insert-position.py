class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        if target < nums[left]:
            return left
        if target > nums[right]:
            return right + 1
        while left < right and right - left > 1:
            mid = (left + right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[left] < target:
            return right
        else:
            return left