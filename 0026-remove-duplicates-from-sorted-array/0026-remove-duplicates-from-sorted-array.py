class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        copied = nums[:]
        for i in copied:
            if hash_table.get(i,0):
                nums.remove(i)
                # nums.append('_')
            else:
                hash_table[i] = 1
        # return nums