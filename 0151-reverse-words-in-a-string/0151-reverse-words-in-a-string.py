class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splited_s = s.split(" ")
        sorted_s = splited_s[::-1]
        answer = ""
        for i in sorted_s:
            if i == '':
                continue
            else:
                answer += i
                answer += " "
        return answer[:-1]