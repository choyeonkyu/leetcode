class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {} # (index, total) -> maximum money till index

        def backtrack(i, total):
            if i >= len(nums):
                return total
            total += nums[i]
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = max(backtrack(i + 3, total), backtrack(i + 2, total))
            return dp[(i, total)]
        return max(backtrack(0, 0), backtrack(1, 0))