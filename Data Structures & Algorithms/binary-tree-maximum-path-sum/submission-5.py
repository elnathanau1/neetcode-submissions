# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = -10000

        
        def helper(root: Optional[TreeNode]) -> (int, int):
            left_true_max = 0
            right_true_max = 0
            if root.left: 
                left_maxes = helper(root.left)
                left_true_max = max(0, left_maxes[0], left_maxes[1])
            
            if root.right: 
                right_maxes = helper(root.right)
                right_true_max = max(0, right_maxes[0], right_maxes[1])

            nonlocal global_max
            global_max = max(
                global_max, 
                left_true_max + right_true_max + root.val
                )
            return (left_true_max + root.val, right_true_max + root.val)



        

        helper(root)

        return global_max