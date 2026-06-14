# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = collections.deque()
        q.append([root, 0])
        answer = []
        while q:
            length = len(q)
            temp = []
            for i in range(length):
                cur, depth = q.popleft()
                if depth % 2 == 0:
                    temp.append(cur.val)
                else:
                    temp = [cur.val] + temp
                if cur.left:
                    q.append([cur.left, depth + 1])
                if cur.right:
                    q.append([cur.right, depth + 1])
            answer.append(temp)
        return answer