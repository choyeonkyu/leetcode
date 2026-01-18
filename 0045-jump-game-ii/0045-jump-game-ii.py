class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        jumps = 0
        farthest = 0
        end = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                end = farthest
                jumps += 1
        return jumps