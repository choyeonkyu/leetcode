class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # import itertools
        # print(help(itertools))
        # ''''chain', 'combinations', 'combinations_with_replacement', 'compress', 'count', 'cycle', 'dropwhile', 'groupby', 'ifilter', 'ifilterfalse', 'imap', 'islice', 'izip', 'izip_longest', 'permutations', 'product', 'repeat', 'starmap', 'takewhile', 'tee''''
        from itertools import permutations
        x = permutations(nums, len(nums))
        ans = []
        for i in x:
            if list(i) not in ans:
                ans.append(list(i))
        return ans