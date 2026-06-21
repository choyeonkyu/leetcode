class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left, right = 0, k-1
        cur_cnt = 0
        for i in s[:right+1]:
            if i in ['a', 'e', 'i', 'o', 'u']:
                cur_cnt += 1
        answer = cur_cnt
        # print(cur_cnt)
        while right < len(s)-1:
            left += 1
            right += 1
            if s[left-1] in ['a', 'e', 'i', 'o', 'u']:
                cur_cnt -= 1
            if s[right] in ['a', 'e', 'i', 'o', 'u']:
                cur_cnt += 1
            # print(left, right, cur_cnt)
            answer = max(answer, cur_cnt)
        return answer