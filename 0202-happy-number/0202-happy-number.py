class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def calc(num):
            temp = []
            div = 10
            while num != 0:
                temp.append((num%div)**2)
                num //= div
            result = sum(temp)
            if result < 10 and (result != 1 and result != 7):
                result = False
            return result
        while n != 1:
            temp_n = calc(n)
            if temp_n == 1 or temp_n == 7:
                return True
            if not temp_n:
                return False
            n = temp_n
        return True