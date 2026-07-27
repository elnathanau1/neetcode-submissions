from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        ret = []
        if root: 
            queue.append(root)

        while queue:
            added = False
            for _ in range(len(queue)):
                node = queue.popleft()
                if not added: 
                    added = True
                    ret.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return ret