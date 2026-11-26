class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        hsh = {}
        for i in s:
            hsh[i] = hsh.get(i,0) + 1
        answer = ""
        while sum(hsh.values()) > 0:
            temp = sorted(hsh.items(),key=lambda x: -x[1])
            for key, val in temp[:2]:
                if val <= 0:
                    continue
                if len(answer) > 0 and answer[-1] == key:
                    return ""
                answer += key
                hsh[key] = val-1
        return answer