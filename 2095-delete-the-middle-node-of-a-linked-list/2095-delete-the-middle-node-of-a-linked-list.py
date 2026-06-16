# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow, fast = head, head
        if not fast.next:
            return None

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        print(slow.val)
        if prev.next is not None:
            prev.next = prev.next.next
        else:
            prev.next = None
        return head