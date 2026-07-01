class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr_num, curr_str = 0, ''
        for i in s:
            if i.isdigit():
                curr_num = 10 * curr_num + int(i)
            elif i == '[':
                stack.append((curr_num, curr_str))
                curr_num, curr_str = 0, ''
            elif i == ']':
                n, s = stack.pop()
                curr_str = s + n*curr_str
            else:
                curr_str += i
        return curr_str