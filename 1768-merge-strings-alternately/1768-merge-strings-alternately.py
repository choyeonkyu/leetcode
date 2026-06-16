class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        answer = ""
        if len(word1) > len(word2):
            for i in range(len(word2)):
                answer += word1[i]
                answer += word2[i]
            answer += word1[i+1:]
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                answer += word1[i]
                answer += word2[i]
            answer += word2[i+1:]
        else:
            for i in range(len(word1)):
                answer += word1[i]
                answer += word2[i]
        return answer