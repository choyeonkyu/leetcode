class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        hash_dict = {}
        inv_hash_dict = {}
        splited_s = s.split(' ')
        if len(splited_s) != len(pattern):
            return False
        for idx, elem in enumerate(pattern):
            cur = hash_dict.get(elem, None)
            inv_cur = inv_hash_dict.get(splited_s[idx], None)
            if cur:
                if cur != splited_s[idx]:
                    return False
            else:
                hash_dict[elem] = splited_s[idx]

            if inv_cur:
                if inv_cur != elem:
                    return False
            else:
                inv_hash_dict[splited_s[idx]] = elem
        return True