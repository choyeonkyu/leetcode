class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import heapq
        nums = nums1+nums2
        heapify(nums)
        if (len(nums1)+len(nums2)) % 2:
            length = (len(nums1)+len(nums2)) // 2
            for i in range(length):
                heapq.heappop(nums)
            return heapq.heappop(nums)
        else:
            length = (len(nums1)+len(nums2)) // 2
            length -= 1
            for i in range(length):
                heapq.heappop(nums)
            temp1 = heapq.heappop(nums)
            temp2 = heapq.heappop(nums)
            return (temp1 + temp2)/2.0
        # if (len(nums1)+len(nums2)) % 2:
        #     length = (len(nums1)+len(nums2)) // 2
        # else:
        #     length = (len(nums1)+len(nums2)) // 2
        #     length -= 1
        # idx1, idx2 = 0, 0
        # for i in range(length):
        #     if nums1[idx1] < nums2[idx2] and idx1 < len(nums1)-1:
        #         idx1 += 1
        #     elif nums1[idx1] >= nums2[idx2] and idx2 < len(nums2)-1:
        #         idx2 += 1
        #     elif nums1[idx1] < nums2[idx2] and idx1 == len(nums1)-1:
        #         idx2 += 1
        #     elif nums1[idx1] >= nums2[idx2] and idx2 == len(nums2)-1:
        #         idx1 += 1
        # return idx1, idx2
            