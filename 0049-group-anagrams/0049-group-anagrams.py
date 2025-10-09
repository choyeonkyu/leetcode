class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_dict = {}
        for s in strs:
            key = ''.join(sorted(s))
            str_dict[key] = str_dict.get(key, []) + [s]
        return str_dict.values()