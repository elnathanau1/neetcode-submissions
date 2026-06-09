# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_indices = {}
        inorder_indices = {}
        for i, val in enumerate(preorder):
            preorder_indices[val] = i
        for i, val in enumerate(inorder):
            inorder_indices[val] = i
    
        def buildTreeHelper(pre_start: int, pre_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
            if pre_start > pre_end:
                return None
            elif pre_start == pre_end:
                return TreeNode(preorder[pre_start])
            
            root = TreeNode(preorder[pre_start])
            root_inorder_index = inorder_indices.get(root.val)
            left_inorder = [in_start, root_inorder_index - 1]
            right_inorder = [root_inorder_index + 1, in_end]
            left_len = left_inorder[1] - left_inorder[0]
            right_len = right_inorder[1] - right_inorder[0]
            left_preorder = [pre_start + 1, pre_start + 1 + left_len]
            right_preorder = [pre_start + 1 + left_len + 1, pre_start + 1 + left_len + 1 + right_len]

            root.left = buildTreeHelper(left_preorder[0], left_preorder[1], left_inorder[0], left_inorder[1])
            root.right = buildTreeHelper(right_preorder[0], right_preorder[1], right_inorder[0], right_inorder[1])

            return root
        
        return buildTreeHelper(0, len(preorder) - 1, 0, len(inorder) - 1)



"""
Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
pre: root, left, right
inorder: left to right



Output: [1,2,3,null,null,null,4]

"""