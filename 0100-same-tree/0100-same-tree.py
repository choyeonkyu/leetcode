# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        queue = collections.deque()
        queue.append((p,q))
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        while queue:
            cur_p, cur_q = queue.popleft()
            if cur_p.val != cur_q.val:
                return False
            if cur_p.left and cur_q.left:
                queue.append((cur_p.left, cur_q.left))
            if cur_p.right and cur_q.right:
                queue.append((cur_p.right, cur_q.right))
            if (cur_p.left and not cur_q.left) or (not cur_p.left and cur_q.left) or (cur_p.right and not cur_q.right) or (not cur_p.right and cur_q.right):
                return False
        return True