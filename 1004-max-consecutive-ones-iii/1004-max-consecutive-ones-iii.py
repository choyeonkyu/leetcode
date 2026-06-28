class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0 if nums[0] == 0 and k == 0 else 1
        left, right = 0, 1
        zero_cnt = 1 if nums[0] == 0 else 0
        answer = 0
        while left <= right and right <= len(nums)-1:
            if zero_cnt < k:
                right += 1
                zero_cnt = zero_cnt + 1 if nums[right-1] == 0 else zero_cnt
                answer = max(answer, right-left)
            elif zero_cnt == k:
                answer = max(answer, right-left)
                right += 1
                zero_cnt = zero_cnt + 1 if nums[right-1] == 0 else zero_cnt
            else:
                left += 1
                zero_cnt = zero_cnt - 1 if nums[left-1] == 0 else zero_cnt
        if zero_cnt == k and nums[-1] == 1:
            answer = max(answer, len(nums)-left)        
        return answer