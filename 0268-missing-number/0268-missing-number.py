class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        compare = set(range(len(nums)+1))
        return list(compare-set(nums))[0]