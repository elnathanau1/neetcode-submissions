from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        queue = deque()
        temp = head
        stack.append(temp)
        queue.append(temp)
        count = 1
        while temp.next:
            temp = temp.next
            stack.append(temp)
            queue.append(temp)
            count += 1
        
        temp = ListNode()
        toggle = True
        while count > 0:
            if toggle:
                nextNode = queue.popleft()
            else:
                nextNode = stack.pop()
            
            temp.next = nextNode
            temp = temp.next
            count -= 1
            toggle = not toggle
        temp.next = None
        

        
"""
0 1 2 3 4 5 6
            | 
            | 

0 6 1 5 2 4 3
6 5 4


0 1 2 3 4 5 6 7
      |  
            | 

7 6 5 4 
0 7 1 6 2 5 3 4
"""