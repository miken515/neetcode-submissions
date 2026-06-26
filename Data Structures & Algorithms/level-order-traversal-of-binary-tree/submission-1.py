# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Solves the Level Order Traversal Of Binary Tree problem.

        Algorithm: BFS (Breadth-First Search)
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(V + E) - visit each vertex and edge once
        Space Complexity: O(V) - queue can contain up to V vertices
        """
        res = []

        q = deque()
        print(q)
        q.append(root)
        print('aft', q)
        while q:  # Iterate until condition fails
            qlen = len(q)
            lvl = []
            
            for i in range(qlen):  # Process each element
                node = q.popleft()

                if node:
                    lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if lvl:
                res.append(lvl)

        return res