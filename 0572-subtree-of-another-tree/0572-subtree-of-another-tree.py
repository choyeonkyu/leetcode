# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) # DFS로 왼쪽 트리부터 서브트리 찾고 같은지 체크
    
    def isSameTree(self, a, b):
        if not a and not b: # 둘 다 None인 경우 같은 거로 판단
            return True
        if not a or not b: # 둘 중 하나만 None인 경우는 다른거로 판단
            return False
        return (a.val == b.val and self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)) # 재귀 함수
