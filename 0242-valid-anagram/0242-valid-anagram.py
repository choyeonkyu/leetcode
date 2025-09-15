class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_hash, t_hash = {}, {}
        for t_letter in t:
            t_hash[t_letter] = t_hash.get(t_letter, 0) + 1
        for s_letter in s:
            s_hash[s_letter] = s_hash.get(s_letter, 0) + 1
        print(t_hash.keys(), s_hash.keys())
        if t_hash.keys() != s_hash.keys():
            return False
        for key, val in t_hash.items():
            if s_hash.get(key) and val == s_hash.get(key):
                continue
            else:
                return False
        return True
        