class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1개 채울래? 2개 채울래? 3개 채울래? (3개는 X2임)
        # n = 1 -> 1
        # n = 2 -> 2
        # n = 3 -> 5(1+1+1, 1+2, 2+1, 3-1, 3-2)
        # n = 4 -> 11(1+1+1+1, 1+2+1, 2+1+1, 1+1+2, 2+2, 3+1, 1+3)
        # n = 5 -> 24(1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 2+3)
        lst = [1, 2, 5, 11, 24]
        if n <= 5:
            return lst[n-1]
        else:
            MOD = 10**9 + 7
            for i in range(6, n+1):
                temp = lst[-1]*2
                temp += lst[i-4]
                lst.append(temp)
            return lst[n-1]%MOD