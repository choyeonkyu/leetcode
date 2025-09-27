class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        answer, n = [], len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                answer.append(matrix[n-j-1][i])
        for i in range(len(matrix)):
            matrix[i] = answer[n*i:n*(i+1)]
            # print(matrix)
        