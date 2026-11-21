class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = {}
        nums.sort()
        for i in range(len(nums)-2):
            val1 = nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                cur_sum = val1 + nums[left] + nums[right]
                if cur_sum == 0:
                    if str(val1)+str(nums[left])+str(nums[right]) not in answer:
                        answer[str(val1)+str(nums[left])+str(nums[right])] = [val1, nums[left], nums[right]]
                    left += 1
                    right -= 1
                elif cur_sum < 0:
                    left += 1
                else:
                    right -= 1
        return answer.values()