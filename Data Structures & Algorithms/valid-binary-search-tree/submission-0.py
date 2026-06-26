# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Solves the Valid Binary Search Tree problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n) - linear scan of input
        Space Complexity: O(1) - minimal extra space used
        """
        
        def isValid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            return isValid(node.left, left, node.val) and isValid(
                node.right, node.val, right
            )

        return isValid(root, float('-inf'), float('inf'))