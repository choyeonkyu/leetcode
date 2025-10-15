class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 더 낮은쪽을 안쪽으로 이동
        start, end = 0, len(height)-1
        cur = (end - start) * min(height[start], height[end])
        while start < end:
            cur = max(cur , ((end - start) * min(height[start], height[end])))
            if height[start] < height[end]:
                start += 1
            elif height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return cur