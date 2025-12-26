# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        if left == 1:
            l = None
        elif left == 2:
            l = head
            head = head.next 
        else:
            for _ in range(left-2):
                head = head.next
            l = head
            head = head.next
            cur = nxt = head
        prev = head
        cur = nxt = head.next
        print(prev.val)
        for _ in range(right - left):
            nxt = nxt.next
            cur.next = prev
            prev = cur
            cur = nxt
        print(head.val, prev.val)
        if l:
            l.next = prev # 1 -> 4
        else:
            dummy.next = prev
        head.next = cur
        return dummy.next