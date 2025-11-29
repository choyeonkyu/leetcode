class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 1 and k != 0 and len(nums) >= k:
            nums[:-k], nums[-k:] = nums[-k:], nums[:-k]
        elif len(nums) != 1 and k != 0 and len(nums) < k:
            k %= len(nums)
            nums[:-k], nums[-k:] = nums[-k:], nums[:-k]
