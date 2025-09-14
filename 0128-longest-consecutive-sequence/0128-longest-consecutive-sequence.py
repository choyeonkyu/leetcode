class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        sorted_nums = sorted(nums)
        answer, cnt = [], 0
        print(sorted_nums)
        for idx, elem in enumerate(sorted_nums):
            if (idx +1 < len(nums)) and (elem + 1 == sorted_nums[idx+1]):
                cnt += 1
            else:
                answer.append(cnt+1)
                cnt = 0
        print(answer)
        return max(answer)