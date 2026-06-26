"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#DFS and Hashmap
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Solves the Clone Graph problem.

        Algorithm: Hash Table/Dictionary
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n) - linear scan plus hash operations
        Space Complexity: O(n) - store up to n elements
        """
        
        oldToNewMap = {}

        def dfs(node):
            if node in oldToNewMap:
                return oldToNewMap[node]

            copy = Node(node.val)
            oldToNewMap[node] = copy

            for nei in node.neighbors:  # Iterate through collection
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None