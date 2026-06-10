# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        temp = head
        nxt = temp.next
        head.next = None
        while nxt is not None:
            nxt_nxt = nxt.next
            nxt.next = temp

            temp = nxt
            nxt = nxt_nxt

        return temp


"""
a <- b    c
     t
          n    
          nn

"""