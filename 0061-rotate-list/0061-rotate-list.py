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
        prev = head
        k %= length
        for _ in range(k):
            cur = cur.next
        while cur.next:
            cur = cur.next
            prev = prev.next
        cur.next = head
        new_head = prev.next
        prev.next = None
        return new_head