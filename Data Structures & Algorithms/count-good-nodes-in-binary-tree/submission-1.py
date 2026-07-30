# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def dfs(root: TreeNode, seenMax: int):
            nonlocal count
            if root.val >= seenMax:
                count += 1
            nextMax = max(seenMax, root.val)
            if root.left:
                dfs(root.left, nextMax)
            if root.right:
                dfs(root.right, nextMax)
            
        dfs(root, float('-inf'))
        return count