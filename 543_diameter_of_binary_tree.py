# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Track the maximum diameter found so far
        self.max_diameter = 0
        
        def depth(node):
            # Base case: if node is None, depth is 0
            if not node:
                return 0
            
            # Recursively calculate depth of left and right subtrees
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # The diameter passing through this node is the sum of left and right depths
            # Update the maximum diameter if this is larger
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            
            # Return the depth of the current subtree (1 + max of left/right)
            return 1 + max(left_depth, right_depth)
        
        # Start the depth calculation from root
        depth(root)
        
        # Return the maximum diameter found
        return self.max_diameter

