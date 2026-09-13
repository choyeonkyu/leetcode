class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        zero_idx = []
        zero_cnt = 0
        answer = 0
        for idx, elem in enumerate(nums):
            zero_cnt += 1 if elem == 0 else 0
            while zero_cnt > 1:
                if nums[start] == 0:
                    zero_cnt -= 1
                start += 1
            answer = max(answer, idx-start)
        return answer
