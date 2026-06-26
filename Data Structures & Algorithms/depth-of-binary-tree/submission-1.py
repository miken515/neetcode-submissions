# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BFS Recursion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Solves the Depth Of Binary Tree problem.

        Algorithm: Queue-based
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n) - depends on problem constraints
        Space Complexity: O(n) - minimal extra space used
        """
        if not root:
            return 0
        
        lvl = 0
        q = deque([root])
        
        while q:  # Iterate until condition fails
            for i in range(len(q)):  # Process each element
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl += 1
        return lvl