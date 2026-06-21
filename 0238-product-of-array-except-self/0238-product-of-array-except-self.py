class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)

        left_cur_prod = 1
        for idx, elem in enumerate(nums): # 1, 1, 2, 6 // 24, 12, 4, 1
            left_product[idx] = left_cur_prod
            left_cur_prod *= elem

        right_cur_prod = 1
        for i in range(len(nums)-1, -1, -1):
            right_product[i] = right_cur_prod
            right_cur_prod *= nums[i]

        answer = [1] * len(nums)
        for i in range(len(nums)):
            answer[i] = left_product[i] * right_product[i]
        return answer