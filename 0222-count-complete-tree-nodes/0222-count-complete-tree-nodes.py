# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.cnt = 0
        self.dfs(root)
        return self.cnt
    def dfs(self, node):
        if not node:
            return
        self.cnt += 1
        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)