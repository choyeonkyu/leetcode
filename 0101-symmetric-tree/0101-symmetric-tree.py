# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        new_root = TreeNode(root.val)
        q = collections.deque()
        q.append(root)
        q.append(new_root)
        while q: # loop for deepcopy
            length = len(q)
            for _ in range(length/2):
                cur_root = q.popleft()
                cur_new_root = q.popleft()
                if cur_root.left:
                    q.append(cur_root.left)
                    cur_new_root.left = TreeNode(cur_root.left.val)
                    q.append(cur_new_root.left)
                if cur_root.right:
                    q.append(cur_root.right)
                    cur_new_root.right = TreeNode(cur_root.right.val)
                    q.append(cur_new_root.right)
        q = collections.deque()
        q.append(root)
        while q: # loop for rotate
            length = len(q)
            for _ in range(length):
                cur = q.popleft()
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        q = collections.deque()
        q.append(root)
        q.append(new_root)
        while q: # loop for compare
            length = len(q)
            for _ in range(length/2):
                cur_root = q.popleft()
                cur_new_root = q.popleft()
                if (cur_root is not None and cur_new_root is not None and cur_root.val != cur_new_root.val) or ((cur_root is None or cur_new_root is None) and not (cur_root is None and cur_new_root is None)):
                    return False
                if cur_root.left:
                    q.append(cur_root.left)
                    q.append(cur_new_root.left)
                if cur_root.right:
                    q.append(cur_root.right)
                    q.append(cur_new_root.right)
        return True
        