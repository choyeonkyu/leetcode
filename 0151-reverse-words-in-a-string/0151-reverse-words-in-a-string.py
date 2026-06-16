class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splited_s = s.split(" ")
        sorted_s = splited_s[::-1]
        words = [i for i in sorted_s if i != ""]
        return " ".join(words)