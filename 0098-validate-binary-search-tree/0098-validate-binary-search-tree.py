# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.answer, self.prev = True, None
        self.inOrder(root)
        return self.answer

    def inOrder(self, root):
        if not root:
            return

        self.inOrder(root.left)
        
        if self.prev:
            if self.prev.val >= root.val:
                self.answer = False
                return 
        
        self.prev = root
        self.inOrder(root.right)