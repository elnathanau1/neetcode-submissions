# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_list = ""
        subRoot_list = ""

        def preorderRoot(root: Optional[TreeNode]):
            nonlocal root_list
            if not root:
                root_list += "#"
                return
            preorderRoot(root.left)
            preorderRoot(root.right)
            root_list += str(root.val)

        def preorderSubRoot(root: Optional[TreeNode]):
            nonlocal subRoot_list
            if not root:
                subRoot_list += "#"
                return
            preorderSubRoot(root.left)
            preorderSubRoot(root.right)
            subRoot_list += str(root.val)
        
        preorderRoot(root)
        preorderSubRoot(subRoot)
        return subRoot_list in root_list