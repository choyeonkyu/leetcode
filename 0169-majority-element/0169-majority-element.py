class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort? O(nlogn)
        # hash? To add hash table O(n) = linear time
        hash_table = {}
        N = len(nums)
        for i in nums:
            hash_table[i] = hash_table.get(i,0) + 1
            if hash_table[i] > N/2:
                return i