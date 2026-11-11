class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        has = {}
        cnt = 1
        for i in s:
            if i in has:
                cnt += 1
                has = {}
                has[i] = 1
            else:
                has[i] = 1
        return cnt