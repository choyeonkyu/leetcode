class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        reversed_x = x[::-1]
        if x == reversed_x:
            return True
        else:
            return False