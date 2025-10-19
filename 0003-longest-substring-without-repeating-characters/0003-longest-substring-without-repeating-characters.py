class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import deque
        ans = deque()
        for i in s:
            ans.append(i)
            if len(list(set(ans))) == len(ans):
                continue
            else:
                ans.popleft()
        return len(ans)