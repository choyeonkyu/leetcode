# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.prev, self.answer = None, 10**6
        self.inOrder(root)
        return self.answer
    def inOrder(self, root):
        if not root:
            return

        self.inOrder(root.left)
        if self.prev:
            if self.answer > root.val - self.prev.val:
                self.answer = root.val - self.prev.val
                print(self.answer)
        self.prev = root
        self.inOrder(root.right)
