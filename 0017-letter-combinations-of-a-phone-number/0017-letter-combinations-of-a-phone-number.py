class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        alphabets = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        def calc(idx, cur):
            if idx == len(digits):
                answer.append(cur)
                return
            for i in alphabets[digits[idx]]:
                calc(idx+1, cur+i)
        answer = []
        calc(0, "")
        return answer