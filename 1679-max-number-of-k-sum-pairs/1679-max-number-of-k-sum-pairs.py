class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        # use Hash {remainder: idx} 4:0 / 3:1
        hash_table = {}
        answer = 0
        for idx, n in enumerate(nums):
            if n in hash_table and hash_table.get(n, False):
                hash_table[n] = [] if len(hash_table[n]) == 1 else hash_table[n][1:]
                answer += 1
            else:
                if len(hash_table.get(k-n, [])) >= 1:
                    hash_table[k-n].append(idx)
                else:
                    hash_table[k-n] = [idx]
        return answer