# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tempHead = ListNode()
        tempHead.next = head
        tempNode = tempHead
        for i in range(n):
            tempNode = tempNode.next
        removeNode = tempHead
        while tempNode.next:
            tempNode = tempNode.next
            removeNode = removeNode.next
        removeNode.next = removeNode.next.next
        return tempHead.next