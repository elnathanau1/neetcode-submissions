"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}
        temp = head
        while temp:
            copies[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            if temp.next:
                copies[temp].next = copies[temp.next]
            
            if temp.random:
                copies[temp].random = copies[temp.random]

            temp = temp.next
        return copies[head] if head in copies.keys() else None