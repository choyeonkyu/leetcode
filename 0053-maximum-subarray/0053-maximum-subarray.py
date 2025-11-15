class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 힌트 1 — “누적합이 음수가 되면 버려라”
        # 어떤 지점까지 더했는데 누적합이 0보다 작아지면, 그걸 계속 끌고 갈 이유가 있을까?

        # 힌트 2 — “부분합은 연속이어야 한다”
        # 중간에 끊고 다시 시작할 수 있다면, 끊는 기준은 뭘까?

        # 힌트 3 — 항상 현재까지의 최댓값을 갱신하라
        # 지금까지 나온 최대 subarray 합을 기록해두고,
        # 계속 갱신해 나가면 된다.
        max_val = 0
        init_sum = 0
        if max(nums) < 0:
            return max(nums)
        for i in range(len(nums)):
            init_sum += nums[i]
            if init_sum < 0:
                init_sum = 0
            else:
                max_val = max(max_val, init_sum)
        return max_val