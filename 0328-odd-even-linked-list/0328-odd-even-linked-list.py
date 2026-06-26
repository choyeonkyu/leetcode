# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not (head and head.next):
            return head
        first_odd, first_even = head, head.next
        odd, even = head, head.next
        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd = odd.next
            odd.next = first_even
            even = even.next
        return first_odd