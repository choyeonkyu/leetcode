class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = ''
        for i in s:
            if i == "*":
                temp = temp[:-1]
            else:
                temp += i
        return temp