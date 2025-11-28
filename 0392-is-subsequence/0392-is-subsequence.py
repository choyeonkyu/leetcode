class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False
        j = 0
        for i in t:
            if i == s[j]:
                j += 1
                if j == len(s):
                    return True

        return True if j == len(s) else False