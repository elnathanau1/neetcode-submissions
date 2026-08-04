# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans_root = ListNode()
        temp_ans = ans_root
        temp_l1 = l1
        temp_l2 = l2
        carryover = 0
        while temp_l1 or temp_l2:
            n1 = 0 if not temp_l1 else temp_l1.val
            n2 = 0 if not temp_l2 else temp_l2.val
            next_num = (n1 + n2 + carryover) % 10
            carryover = (n1 + n2 + carryover) // 10
            temp_ans.next = ListNode(next_num)
            temp_ans = temp_ans.next

            if temp_l1:
                temp_l1 = temp_l1.next
            if temp_l2:
                temp_l2 = temp_l2.next
            
        if carryover > 0:
            temp_ans.next = ListNode(1)

        return ans_root.next
                
