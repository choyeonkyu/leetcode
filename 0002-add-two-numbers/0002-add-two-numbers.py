# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2, carry = 0):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not l1 and not l2 and carry == 0:
            return None
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        answer = ListNode()
        cur_sum = v1 + v2 + carry
        answer.val = cur_sum % 10
        answer.next = self.addTwoNumbers(l1.next if l1 else None , l2.next if l2 else None , cur_sum // 10)
        return answer
