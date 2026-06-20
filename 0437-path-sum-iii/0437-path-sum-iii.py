# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.targetSum = targetSum
        self.answer = 0
        self.dfs(root, [])
        return self.answer
        
    def dfs(self, node, routes):
        if not node:
            return
        routes.append(node.val)
        total_sum = sum(routes)
        for i in routes:
            if total_sum == self.targetSum:
                self.answer += 1
                # print(routes, i)
            total_sum -= i
        self.dfs(node.left, routes)
        self.dfs(node.right, routes)
        routes.pop()