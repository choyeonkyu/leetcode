class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        temp_left, temp_right = intervals[0]
        answer = []
        for left, right in intervals:
            if left <= temp_right and temp_right <= right:
                temp_right = right
            elif temp_right < left:
                answer.append([temp_left, temp_right])
                temp_left, temp_right = left, right
        if [temp_left, temp_right] not in answer:
            answer.append([temp_left, temp_right])
        return answer