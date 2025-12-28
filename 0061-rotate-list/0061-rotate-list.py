# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if k == 0:
            return head
        if not head or not head.next:
            return head
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        cur = head
        prev = ListNode(0)
        prev.next = head
        while cur.next:
            cur = cur.next
            prev = prev.next
        cur.next = head
        prev.next = None
        return self.rotateRight(cur, (k%length)-1)