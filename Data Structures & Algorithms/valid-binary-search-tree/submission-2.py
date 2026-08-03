# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, maxVal, minVal):
            if not root:
                return True
            if root.val >= maxVal or root.val <= minVal:
                return False
            return isValid(root.left, root.val, max(minVal, float("-inf"))) and isValid(root.right, min(float("inf"), maxVal), root.val)
        return isValid(root, float('inf'), float("-inf"))