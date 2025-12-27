class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 1:
            return 1
        points.sort()
        # find minimum interval
        cnt = 1
        temp_s, temp_e = points[0]
        for start, end in points[1:]:
            if temp_e >= start:
                temp_s = start
                if temp_e >= end:
                    temp_e = end
            else:
                temp_s, temp_e = start, end
                cnt += 1
        return cnt