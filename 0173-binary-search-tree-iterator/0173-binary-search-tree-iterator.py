# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """

        self.tree = self.buildGraph(root)
        self.prev = None
        self.inorder_list = []
        self.inOrder(self.tree)
        print(self.inorder_list)

    def buildGraph(self, node):
        if not node:
            return
        tree = TreeNode(node.val)
        if node.left:
            tree.left = self.buildGraph(node.left)
        if node.right:
            tree.right = self.buildGraph(node.right)
        return tree
        
    def inOrder(self, node):
        if not node:
            return
        self.inOrder(node.left)
        self.inorder_list.append(node.val)
        self.inOrder(node.right)

    def next(self):
        """
        :rtype: int
        """
        temp = self.inorder_list[0]
        self.inorder_list = self.inorder_list[1:]
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if len(self.inorder_list) > 0 else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()