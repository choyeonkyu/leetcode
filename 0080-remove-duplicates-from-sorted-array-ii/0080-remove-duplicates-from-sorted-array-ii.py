class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {} # declare hash table for counting the number of each nums in array
        copied_nums = nums[:]
        for i in copied_nums:
            hash_table[i] = hash_table.get(i, 0) + 1
            if hash_table[i] > 2:
                nums.remove(i)
        # return nums