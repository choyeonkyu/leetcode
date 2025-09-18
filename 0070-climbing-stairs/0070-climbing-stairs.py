import itertools
from itertools import permutations, combinations
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def factorial(x):
            if x == 0:
                return 0
            ret = 1
            for num in range(1, x+1):
                ret *= num
            return ret
        # print(factorial(2), factorial(3))
        min_num = n // 2
        answer = 0
        for i in range(0, min_num+1):
            print(answer)
            num_2 = i
            num_1 = (n-(2*i))
            print(num_1, num_2)
            if num_2 == 0 or num_1 == 0:
                answer += 1
                continue
            answer += factorial(num_1 + num_2) / (factorial(num_1) * factorial(num_2))
        return answer