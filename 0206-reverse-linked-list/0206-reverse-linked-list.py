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
        if not head:
            return
        # head는 포인터
        prev = None
        curr = head # 1
        nxt = head.next # 2
        while nxt:
            curr.next = prev # 1 - None
            prev = curr # 1
            curr = nxt # 2
            nxt = nxt.next
        curr.next = prev
        return curr