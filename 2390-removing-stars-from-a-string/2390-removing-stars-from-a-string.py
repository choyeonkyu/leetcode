class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 문자열에 이렇게 연산하는건 성능이 좋지 않음 (매번 복사가 일어남)
        # list에 연산 후, 맨 마지막에 join
        temp = []
        for i in s:
            if i == "*":
                temp.pop()
            else:
                temp.append(i)
        return ''.join(temp)