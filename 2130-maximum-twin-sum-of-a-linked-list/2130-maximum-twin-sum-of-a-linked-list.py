# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        reversed_head = ListNode()
        rev_cur = reversed_head
        cur = head
        while cur:
            temp = ListNode(cur.val)
            temp.next = rev_cur
            rev_cur = temp
            cur = cur.next
        answer = float('-inf')
        cur = head
        while cur:
            answer = max(answer, cur.val+rev_cur.val)
            cur = cur.next
            rev_cur = rev_cur.next
        return answer