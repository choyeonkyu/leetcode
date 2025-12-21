class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for idx, elem in enumerate(numbers):
            val = hash_map.get(elem,-1)
            if val>=0:
                return [hash_map[elem],idx+1]
            else:
                hash_map[target-elem] = idx+1