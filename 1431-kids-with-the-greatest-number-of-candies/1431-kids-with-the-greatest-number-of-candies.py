class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        cur_max = max(candies)
        answer = []
        for i in candies:
            if i + extraCandies >= cur_max:
                answer.append(True)
            else:
                answer.append(False)
        return answer