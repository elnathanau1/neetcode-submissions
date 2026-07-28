# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:    
            if not root and not subRoot:
                return True
            if root and not subRoot or not root and subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)
        
        if isSame(root, subRoot):
            return True
        if root.left and self.isSubtree(root.left, subRoot):
            return True
        if root.right and self.isSubtree(root.right, subRoot):
            return True
        return False

            