# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack: list[tuple[TreeNode | None, int|None, int|None]] = [(root, None, None)]

        while stack:
            node, min_val, max_val = stack.pop()
           
            if node is None:
                continue
            
            if min_val is not None and node.val <= min_val:
                return False
            elif max_val is not None and node.val >= max_val: 
                return False
            else:
                stack.append((node.left, min_val, node.val))
                stack.append((node.right, node.val, max_val))
            
            
        return True
