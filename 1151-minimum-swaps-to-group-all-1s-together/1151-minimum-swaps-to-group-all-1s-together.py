class Solution(object):
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        total_sum = sum(data)
        start, end = 0, total_sum
        cur_sum = sum(data[start:end])
        max_sum = cur_sum
        while end < len(data):
            start += 1
            end += 1
            if data[start-1] == 1:
                cur_sum -= 1
            if data[end-1] == 1:
                cur_sum += 1
            max_sum = max(cur_sum, max_sum)
        return total_sum - max_sum