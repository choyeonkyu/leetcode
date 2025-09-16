class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        # [11, 13, 15, 17] 과 [15, 17, 11, 13], [13, 15, 17, 11]에서 통용되려면?
        while len(nums)>2:
            if nums[mid] > nums[right]:
                nums = nums[mid + 1:]
                right = len(nums) - 1
                mid = (left + right) // 2
            else:
                nums = nums[:mid+1]
                right = len(nums) - 1
                mid = (left + right) // 2
        return min(nums)
        