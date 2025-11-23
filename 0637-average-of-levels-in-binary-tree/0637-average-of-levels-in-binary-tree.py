# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        from collections import deque
        q = deque()
        q.append((root, 0))
        def bfs(q):
            answer, temp = [], []
            past_node_level = 0
            while q:
                cur = q.popleft()
                val = cur[0].val
                level = cur[1]
                if len(answer) < level:
                    answer.append(float(sum(temp))/len(temp))
                    temp = []
                temp.append(val)
                if cur[0].left:
                    q.append((cur[0].left, cur[1]+1))
                if cur[0].right:
                    q.append((cur[0].right, cur[1]+1))
            if temp:
                answer.append(float(sum(temp))/len(temp))
            return answer
        return bfs(q)