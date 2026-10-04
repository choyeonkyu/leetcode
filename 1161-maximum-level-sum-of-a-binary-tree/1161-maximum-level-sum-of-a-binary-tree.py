# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q = collections.deque()
        q.append(root)
        max_level, max_val = 1, root.val
        cur_level = 0
        while q:
            cur_level += 1
            length = len(q)
            temp = []
            for _ in range(length):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            summed = sum(temp)
            if summed > max_val:
                max_val = summed
                max_level = cur_level

        return max_level
        