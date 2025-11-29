"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None # handle corner case that input data is None.
        old_to_new = {} # record whether node is already copied or not.
        def dfs(n):
            if n is None:
                return None
            if n in old_to_new: # for random pointer?
                return old_to_new[n]
            copied = Node(n.val)
            old_to_new[n] = copied
            if n.next:
                copied.next = dfs(n.next)
            if n.random:
                copied.random = dfs(n.random)
            return copied
        return dfs(head)