class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, right, total_sum = 0, 0, 0
        answer = 10**10
        while right >= left:
            if total_sum >= target:
                answer = min(answer, right-left)
                total_sum -= nums[left]
                left += 1
            elif right < len(nums):
                total_sum += nums[right]
                right += 1 
            else:
                if answer == 10**10:
                    return 0
                else:
                    return answer
        