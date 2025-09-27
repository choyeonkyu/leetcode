class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # two-pointer로 접근해야 하는 문제임.
        s_dict, n, l, r, maxlen = {}, len(s), 0, 0, 0
        for idx, elem in enumerate(s):
            s_dict[elem] = s_dict.get(elem, 0) + 1
            cur_len = idx - l + 1
            if cur_len - max(s_dict.values()) <= k:
                maxlen = max(maxlen, cur_len)
            else: # 만약 현 위치에서 k개 이상 replace를 해야한다면 left pointer를 
                  # 이동시켜야 할 때 인것임
                s_dict[s[l]] -= 1
                l += 1
        return maxlen