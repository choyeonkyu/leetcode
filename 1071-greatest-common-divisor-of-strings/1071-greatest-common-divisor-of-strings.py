class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) < len(str2):
            tar, divisor = str2, str1
        elif len(str1) == len(str2):
            if str1 == str2:
                return str1
            else:
                return ""
        else:
            tar, divisor = str1, str2
        
        answer = ''
        for i in range(1, len(divisor)+1):

            if len(tar) % i == 0 and len(divisor) % i == 0 and (divisor[:i] * (len(tar)//i)) == tar and (divisor[:i] * (len(divisor)//i)) == divisor:
                answer = divisor[:i]
        return answer
