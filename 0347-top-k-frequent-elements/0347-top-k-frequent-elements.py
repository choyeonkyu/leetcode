class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = {}
        for i in nums:
            cnt[i] = cnt.get(i, 0) + 1
        # print(cnt)
        cnt_lst = []
        for key, value in cnt.items():
            cnt_lst.append([key, value])
        cnt_lst.sort(key = lambda x: -1*x[1])
        answer = []
        for j in range(k):
            answer.append(cnt_lst[j][0])
        return answer