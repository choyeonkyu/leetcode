class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        cnt = 0
        while start < end:
            if nums[start] == nums[end]:
                start += 1
                end -= 1
                continue
            if nums[start] < nums[end]:
                nums[start+1] = nums[start] + nums[start+1]
                nums.pop(start)
                end -= 1
            elif nums[start] > nums[end]:
                nums[end-1] = nums[end] + nums[end-1]
                nums.pop(end)
                end -= 1
            cnt += 1
        return cnt