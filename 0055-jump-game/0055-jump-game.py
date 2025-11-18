class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 가장 멀리 갈 수 있는 곳으로 업데이트를 해야한다
        max_loc = 0
        for idx, elem in enumerate(nums):
            if idx > max_loc:
                return False
            max_loc = max(max_loc, idx+elem)
        return True