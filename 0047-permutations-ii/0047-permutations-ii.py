class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        x = permutations(nums, len(nums))
        ans = []
        for i in x:
            if list(i) not in ans:
                ans.append(list(i))
        return ans