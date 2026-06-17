# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.answer = 0
        self.dfs(root, 0)
        
        return self.answer

    def dfs(self, node, level):
        if not node:
            self.answer = max(self.answer, level)
            return 
        self.dfs(node.left, level+1)
        self.dfs(node.right, level+1)