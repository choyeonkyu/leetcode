class Solution(object):
    def kBigIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        # print(help(heapq))
        left, right = [], [] # 왼쪽, 오른쪽에서 제일 작은애들 k개 관리.
        heapq.heapify(left)
        heapq.heapify(right)
        # print(type(left))
        left_cand_idx, right_cand_idx = [], [] # 조건 만족한애들 인덱스 관리
        for i in range(len(nums)):
            if len(left) < k:
                heapq.heappush(left, -1 * nums[i])
                continue
            if left[0] > -1*nums[i]:
                left_cand_idx.append(i)
            else:
                heapq.heappushpop(left, -1 * nums[i])

        for i in range(len(nums)-1, -1, -1):
            if len(right) < k:
                heapq.heappush(right, -1 * nums[i])
                continue
            if right[0] > -1 * nums[i]:
                right_cand_idx.append(i)
            else:
                heapq.heappushpop(right, -1 * nums[i])
        return len(list(set(left_cand_idx) & set(right_cand_idx)))