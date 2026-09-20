class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rec = [float('-inf')] * len(nums)
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]
        rec[0] = nums[0]
        rec[1] = max(nums[1], rec[0])
        for i in range(2, len(nums)):
            rec[i] = max(rec[i-2]+nums[i], rec[i-1])
        return rec[-1]