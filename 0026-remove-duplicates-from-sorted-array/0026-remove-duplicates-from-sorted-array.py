class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        j = 0

        for i in range(len(nums)):
            val = nums[i]
            hash_table[val] = hash_table.get(val, 0) + 1
            nums[j] = val
            if hash_table[val] <= 1:
                j += 1
        return j