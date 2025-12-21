# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.preorder_list = []
        self.preOrder(root)
        if len(self.preorder_list) >= 2:
            root.left = None
            for i in self.preorder_list[1:]:
                root.right = TreeNode(i)
                root = root.right
    def preOrder(self, root):
        if not root:
            return
        self.preorder_list.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)