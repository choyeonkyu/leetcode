# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return
        cur = head
        temp_list = []
        while cur:
            temp_list.append(cur.val)
            cur = cur.next
        temp_list.sort()
        dummy = ListNode()
        cur = dummy
        for i in temp_list:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next