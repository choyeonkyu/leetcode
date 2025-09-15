# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = cur = ListNode(0) # dummy와 cur가 같은 더미 노드를 가리킵니다.(dummy는 결과 리스트의 시작을 기억하는 역할, cur는 현재 끝을 가리키는 역할)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next # cur를 새로 붙인 노드(결과 리스트의 새 끝)로 이동.
        cur.next = list1 if list1 else list2 # 마지막 남은 노드 하나 붙이는 용도
        return dummy.next
