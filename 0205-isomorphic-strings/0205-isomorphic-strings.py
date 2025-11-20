class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(str(s))
        t = list(str(t))
        hash_table = {}
        def validate(s,t):
            for idx, elem in enumerate(s):
                ret = hash_table.get(elem,False)
                if ret == t[idx]:
                    continue
                elif not ret:
                    hash_table[elem] = t[idx]
                else:
                    print(ret, t[idx])
                    return False
            return True
        if len(list(set(s))) >= len(list(set(t))):
            answer = validate(t,s)
        else:
            answer = validate(s,t)
        return answer