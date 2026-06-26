# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Solves the Binary Tree Right Side View problem.

        Algorithm: Queue-based
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n) - depends on problem constraints
        Space Complexity: O(n) - minimal extra space used
        """
        q = deque([root])
        res = []

        while q:  # Iterate until condition fails
            rightside = None
            qlen = len(q)

            for i in range(qlen):  # Process each element
                node = q.popleft()  
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)


            if rightside:
                res.append(rightside.val)
        
        return res