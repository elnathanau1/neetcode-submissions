from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []

        retList = []
        queue = deque()
        queue.append(root)
        while queue:
            levelList = []
            for _ in range(len(queue)):
                node = queue.popleft()
                levelList.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            retList.append(levelList)
        return retList