# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.cur_max = 0
        self.dfs(root, 0, 'start')
        return self.cur_max

    def dfs(self, node, cum_cnt, prev_dir):
        if not node:
            self.cur_max = max(self.cur_max, cum_cnt-1)
            # print(prev_dir, cum_cnt)
            return
        if prev_dir == 'left':
            self.dfs(node.left, 1, 'left')
            self.dfs(node.right, cum_cnt+1, 'right')
        elif prev_dir == 'right':
            self.dfs(node.left, cum_cnt+1, 'left')
            self.dfs(node.right, 1, 'right')
        else:
            self.dfs(node.left, cum_cnt+1, 'left')
            self.dfs(node.right, cum_cnt+1, 'right')