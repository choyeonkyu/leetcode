# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        stack = [root] if root else []
        answer = [[root.val]] if root else []
        while stack:
            # print(answer)
            temp, stack = self.traverse(stack)
            if temp:
                answer.append(temp)
        return answer
        
    def traverse(self, stack):
        temp, new = [], []   
        for _ in range(len(stack)):
            cur = stack[0]
            stack = stack[1:]
            if cur.left:
                temp.append(cur.left.val)
                new.append(cur.left)
            if cur.right:
                temp.append(cur.right.val)
                new.append(cur.right)
        return temp, new
