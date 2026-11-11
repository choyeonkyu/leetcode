class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        import math
        factors = []
        sqt = int(floor(pow(n,0.5)))
        for i in range(1, sqt+1):
            if n%i == 0:
                factors.append(i)
                factors.append(n/i)
        factors = list(set(factors))
        if len(factors) < k:
            return -1
        factors.sort()
        return factors[k-1]