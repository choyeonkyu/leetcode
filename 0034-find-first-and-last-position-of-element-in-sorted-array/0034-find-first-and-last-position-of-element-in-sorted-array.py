class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums)-1
        while left < right-1: # 2번 돌립시다.
            mid = (left+right)/2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            answer = [left, -1]
        elif nums[right] == target:
            answer = [right, -1]
        else:
            return [-1, -1]
        left, right = 0, len(nums)-1
        while left < right-1:
            mid = (left+right)/2
            if nums[mid] == target:
                left = mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            answer[1] = right
        elif nums[left] == target:
            answer[1] = left
        else:
            return [-1, -1]
        return answer