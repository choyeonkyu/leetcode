class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        multipled = 1
        temp = nums[:]
        answer = []
        cnt = 0
        while 0 in temp:
            cnt += 1
            temp.remove(0)
        else:
            if temp:
                for i in temp:
                    multipled *= i
            # else:
            #     return [0] * len(nums)
            if cnt > 1:
                return [0] * len(nums)
            elif cnt == 1:
                for i in nums:
                    if i == 0:
                        answer.append(multipled)
                    else:
                        answer.append(0)
                return answer
            else:
                for i in nums:
                    answer.append(multipled/i)
                return answer        