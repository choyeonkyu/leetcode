# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.answer = 0
        self.dfs(root, float('-inf'))
        return self.answer

    def dfs(self, node, prev_max):
        if not node:
            return
        if max(node.val, prev_max) == node.val:
            self.answer += 1
        self.dfs(node.left, max(node.val, prev_max))
        self.dfs(node.right, max(node.val, prev_max))