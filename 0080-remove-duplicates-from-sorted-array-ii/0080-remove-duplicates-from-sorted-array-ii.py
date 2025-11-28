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
            
            # 2번 이하이면 유효한 위치에 복사
            if hash_table[val] <= 2:
                nums[j] = val
                j += 1
        
        return j