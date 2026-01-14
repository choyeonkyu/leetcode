class Solution(object):
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.memo = {}
        return self.find(s, wordDict)
    
    def find(self, s, wordDict):
        if s in self.memo:
            return self.memo[s]
        if s == "":
            return True
        for i in wordDict:
            if s.startswith(i):
                if self.find(s[len(i):], wordDict):
                    self.memo[s] = True
                    return True
        self.memo[s] = False
        return False