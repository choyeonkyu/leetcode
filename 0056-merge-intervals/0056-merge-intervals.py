class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x: x[0])
        answer = []
        temp_left, temp_right = intervals[0][0], intervals[0][1]
        for (left, right) in intervals:
            if temp_right < left:
                print('if', left, right)
                answer.append([temp_left, temp_right])
                temp_left, temp_right = left, right
            elif temp_left <= left and temp_right >= right:
                print('elif 1',left, right)
            elif temp_left <= left and temp_right < right: 
                print('elif 2',left, right)
                temp_right = right
        answer.append([temp_left, temp_right])
        return answer