class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] == 9:
            x = 0
            for i in digits:
                x *= 10
                x += i
            x = int(x) + 1
            x = str(x)
            digits = []
            for i in x:
                digits.append(int(i))
        else:
            digits[-1] = digits[-1] + 1
        return digits