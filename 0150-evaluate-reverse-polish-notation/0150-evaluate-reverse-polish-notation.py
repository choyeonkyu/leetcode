class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        def calc(x,y,op):
            if op == "+":
                answer = x+y
            elif op == "-":
                answer = y-x
            elif op == "*":
                answer = x*y
            else:
                answer = y//x
                if x*y < 0 and y%x != 0:
                    answer += 1     
            return int(answer)
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                x = stack.pop()
                y = stack.pop()
                # print(x,y,i)
                stack.append(calc(x,y,i))
            else:
                stack.append(int(i))
        return stack[-1]