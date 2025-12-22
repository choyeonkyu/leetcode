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
        def cntLeft(tree):
            cnt = 1
            while tree.left:
                cnt += 1
                tree = tree.left
            return cnt
        def cntRight(tree):
            cnt = 1
            while tree.right:
                cnt += 1
                tree = tree.right
            return cnt
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        elif root.left and not root.right:
            return 2
        left, right = cntLeft(root), cntRight(root)
        if left == right:
            return 2**left - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1