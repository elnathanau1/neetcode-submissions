# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(root: Optional[TreeNode]) -> (int, int):
            if not root or (not root.left and not root.right):
                return (0, 0)

            left_edge = 0
            right_edge = 0
            left = 0
            right = 0
            if root.left:
                left = max(dfs(root.left))
                left_edge += 1
            if root.right:
                right = max(dfs(root.right))
                right_edge += 1
            
            nonlocal max_diameter
            max_diameter = max(left + right + left_edge + right_edge, max_diameter)
            return (left + left_edge, right + right_edge)


        left, right = dfs(root)
        max_diameter = max(left + right, max_diameter)
        return max_diameter