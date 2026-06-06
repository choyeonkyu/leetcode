# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = answer = ListNode()
        cur1, cur2 = l1, l2
        upper = 0
        while cur1 or cur2:
            if cur1 and cur2:
                temp_val = cur1.val + cur2.val + upper
            elif cur1:
                temp_val = cur1.val + upper
            elif cur2:
                temp_val = cur2.val + upper
            upper = 1 if temp_val > 9 else 0
            temp_val = temp_val - 10 if upper == 1 else temp_val
            head.val = temp_val
            
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None

            if cur1 or cur2:
                head.next = ListNode()
                head = head.next
            elif upper == 1:
                head.next = ListNode(1)
        return answer