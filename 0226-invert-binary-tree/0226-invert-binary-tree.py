# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root
        q = collections.deque()
        q.append(root)
        while q:
            length = len(q)
            for _ in range(length):
                cur = q.popleft()
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root