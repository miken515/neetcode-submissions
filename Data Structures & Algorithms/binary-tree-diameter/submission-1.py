# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Solves the Binary Tree Diameter problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n) - linear scan of input
        Space Complexity: O(1) - minimal extra space used
        """
        largest = 0

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal largest
            largest = max(largest, left + right)
            return 1 + max(left, right)
    
        dfs(root)
        return largest