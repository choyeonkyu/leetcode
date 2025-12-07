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
        if not root:
            return 0
        q = collections.deque()
        q.append((root, 1))
        while q:
            curr, level = q.popleft()
            if curr.left:
                q.append((curr.left, level+1))
            if curr.right:
                q.append((curr.right, level+1))
        return level