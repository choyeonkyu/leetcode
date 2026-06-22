class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        cur, cur_max = 0, 0
        for i in gain:
            cur += i
            cur_max = max(cur, cur_max)
        return cur_max
