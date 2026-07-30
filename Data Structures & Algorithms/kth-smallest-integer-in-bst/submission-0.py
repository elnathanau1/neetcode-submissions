# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        temp = -1
        def inorder(root: Optional[TreeNode]):
            nonlocal k, temp
            if k <= 0 or not root:
                return
            if root.left:
                inorder(root.left)
                if k <= 0 or not root:
                    return
            k -= 1
            temp = root.val
            if k == 0:
                return 
            if root.right:
                inorder(root.right)
        inorder(root)
        return temp

"""
inorder traversal


"""