class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        comp = defaultdict()
        for i in nums:
            if i in comp:
                return i
            else:
                comp[i] = 1