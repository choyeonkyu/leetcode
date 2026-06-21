class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total_multiple = 1
        zero_cnt = 0
        for i in nums:
            total_multiple *= i
            if i == 0:
                zero_cnt += 1 
        if zero_cnt >= 2:
            return [0] * len(nums)
        hash_table = {}
        answer = []
        
        if total_multiple == 0:
            for idx, i in enumerate(nums):
                if i == 0:
                    
                    if i in hash_table:
                        answer.append(hash_table[i])
                    else:
                        copied_nums = nums[:]
                        copied_nums.pop(idx)
                        import numpy as np
                        nums_np = np.array(copied_nums)
                        temp_total = nums_np.prod()
                        hash_table[i] = temp_total
                        answer.append(temp_total)
                else:
                    answer.append(0)
                    
        else:
            for i in nums:
                if i in hash_table:
                    answer.append(hash_table[i])
                else:
                    temp = total_multiple/i
                    hash_table[i] = temp
                    answer.append(temp)
        return answer
