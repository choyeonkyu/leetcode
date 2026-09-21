class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heapify(nums)
        n = heapq.nlargest(k, nums)
        heapify(n)
        return n[0]