# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        small, big = ListNode(), ListNode()
        small_cur, big_cur = small, big
        cur = head
        while cur:
            if cur.val < x:
                small_cur.next = ListNode(cur.val)
                small_cur = small_cur.next
            else:
                big_cur.next = ListNode(cur.val)
                big_cur = big_cur.next
            cur = cur.next
        small_cur.next = big.next
        return small.next
        