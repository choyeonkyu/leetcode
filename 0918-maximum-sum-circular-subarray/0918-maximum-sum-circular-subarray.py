class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = cur_sum = nums[0]
        for i in nums[1:]:
            cur_sum = max(i, i+cur_sum)
            max_sum = max(cur_sum, max_sum)

        min_sum = cur_sum = nums[0]
        for i in nums[1:]:
            cur_sum = min(i, i+cur_sum)
            min_sum = min(cur_sum, min_sum)
        
        if max_sum < 0:
            return max_sum
        else:
            return max(max_sum, sum(nums) - min_sum)