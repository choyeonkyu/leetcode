class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        # two pointer
        # 서로 조이면서 올라가면 계속 가, 내려가면 채워. 원래 자기보다 높은애 나타나면 걔로 기준 바꿔.그러다가 서로 만나면 끝
        answer = 0
        left_max = right_max = 0
        while right > left:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                answer += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                answer += right_max - height[right]
                right -= 1
        return answer