class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import deque
        ans = deque()
        for i in s:
            # if i not in ans:
            #     ans.append(i)
            # else:
            #     ans.popleft()
            #     ans.append(i)
            ans.append(i)
            if len(list(set(ans))) == len(ans):
                continue
            else:
                ans.popleft()
            print(ans)
        return len(ans)
            # print(help(ans)) # append, appendleft, pop, popleft