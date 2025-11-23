# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.prev, self.i = None, 0
        self.inOrder(root, k)
        return self.answer
    def inOrder(self, root, k):
        if not root:
            return
        self.inOrder(root.left, k)
        self.prev = root
        if self.prev:
            self.i += 1
            if self.i == k:
                self.answer = root.val
                return
        self.inOrder(root.right, k)