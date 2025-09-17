class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = []
        for i in range(32):
            i -= 31
            i = abs(i)
            # print(i)
            div = 2**i
            # print(div)
            if n // div >= 1:
                binary.append(1)
                n = n%div
            else:
                binary.append(0)
        reverse = binary[::-1]
        print(reverse)
        answer = 0
        for i, num in enumerate(reverse):
            i -= 31
            i = abs(i)
            mul = 2**i
            if num == 1:
                answer += mul
            else:
                continue
        return answer