# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(root: Optional[TreeNode]) -> (int, int): 
            if not root:
                return (0, 0)
            left = 0
            right = 0
            if root.left:
                left = max(dfs(root.left)) + 1
            if root.right: 
                right = max(dfs(root.right)) + 1
            
            if abs(left - right) > 1:
                nonlocal balanced
                balanced = False
            
            return (left, right)
            
        dfs(root)
        return balanced
            