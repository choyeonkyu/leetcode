class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x:x[1])
        cur_end = intervals[0][1]
        answer = 0
        for start, end in intervals[1:]:
            if cur_end <= start:
                cur_end = end
            else:
                answer += 1
        return answer