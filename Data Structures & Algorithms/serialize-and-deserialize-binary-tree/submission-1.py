from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: 
            return ""
        string = ""
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            next_level = False
            for _ in range(level_size):
                node = queue.popleft()
                if not node:
                    string += "#,"
                else:
                    string += f"{node.val},"
                    queue.append(node.left)
                    queue.append(node.right)
                    if node.left or node.right:
                        next_level = True
            if not next_level:
                break
        return string[:-1]
        
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        vals = data.split(',')
        if len(vals) == 1:
            return TreeNode(vals[0])
        root = TreeNode(vals[0])
        nodes = [None] * len(vals)
        nodes[0] = root
        slow = 0
        fast = 1
        while fast + 1 < len(vals):
            if vals[fast] != '#':
                nodes[fast] = TreeNode(vals[fast])
            if vals[fast + 1] != '#':
                nodes[fast + 1] = TreeNode(vals[fast + 1])
            if nodes[slow]:
                nodes[slow].left = nodes[fast]
                nodes[slow].right = nodes[fast + 1]
            slow += 1
            while vals[slow] == '#':
                slow += 1
            fast += 2
        
        return nodes[0]
