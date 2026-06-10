# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1, None)
        temp = dummy_head

        l1 = list1
        l2 = list2
        
        while l1 or l2:
            if not l1: 
                temp.next = l2
                l2 = l2.next
            elif not l2:
                temp.next = l1
                l1 = l1.next
            elif l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        return dummy_head.next