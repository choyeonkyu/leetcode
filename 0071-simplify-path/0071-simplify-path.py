class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        splitted = path.split('/')
        stack = []
        for i in splitted[1:]:
            if i == '.':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            elif i == '':
                continue
            else:
                stack.append(i)
        return '/'+'/'.join(stack)