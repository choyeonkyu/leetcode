class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        ref = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        answer = []
        def dfs(cur, idx):
            if idx == len(digits):
                answer.append(cur)
                return
            chars = ref[digits[idx]]
            for i in chars:
                dfs(cur+i, idx+1)
        dfs('', 0)
        return answer