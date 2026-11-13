# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        """
        if not root or root in nodes:
            return root
        l = self.lowestCommonAncestor(root.left, nodes)
        r = self.lowestCommonAncestor(root.right, nodes)
        return l or r if not(l and r) else root