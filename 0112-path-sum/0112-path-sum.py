# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, cur_sum):
        if not node:
            return
        cur_sum += node.val
        if node.left:
            self.dfs(node.left, cur_sum)
        if node.right:
            self.dfs(node.right, cur_sum)
        if not (node.left or node.right):
            if cur_sum == self.targetSum:
                self.answer = True

    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        self.targetSum = targetSum
        self.answer = False
        self.dfs(root, 0)
        return self.answer

    