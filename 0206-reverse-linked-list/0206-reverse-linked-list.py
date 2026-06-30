# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        prev = None
        cur = head
        while cur is not None:
            nxt = cur.next # 3  4
            cur.next = prev # 2 -> 1    3 -> 2
            prev = cur # 2  3
            cur = nxt # 3   4
        return prev