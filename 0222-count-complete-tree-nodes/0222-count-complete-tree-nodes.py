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
        if not root:
            return 0
        q = collections.deque()
        q.append(root)
        cnt = 1
        while q:
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
                cnt += 1
            if cur.right:
                q.append(cur.right)
                cnt += 1
        return cnt
        ## dfs 도전해보기
        # if not root:
        #     return 0
        # cur = root
        # right_cnt = 1
        # stack = [cur]
        # while cur.right:
        #     right_cnt += 1
        #     stack.append(cur)
        #     cur = cur.right
        # print(2**right_cnt-1)
        # print(len(stack))
        # while stack