"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = set()
        createdNodes = {}
        oldNodes = {}

        def cloneNode(node: Optional['Node']) -> Optional['Node']:
            if not node: 
                return None

            if node.val not in oldNodes.keys():
                oldNodes[node.val] = node

            if node.val in createdNodes.keys():
                return createdNodes[node.val]

            newNode = Node(node.val)
            createdNodes[node.val] = newNode

            for neighborNode in node.neighbors:
                cloneNode(neighborNode)
            
            return newNode
        
        cloneNode(node)
        for key in createdNodes.keys():
            neighbors = []
            for neighborNode in oldNodes[key].neighbors:
                neighbors.append(createdNodes[neighborNode.val])
            createdNodes[key].neighbors = neighbors
        
        return createdNodes[node.val]
