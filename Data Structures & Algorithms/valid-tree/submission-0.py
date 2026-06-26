# Valid Tree Solution
#
# This solution implements an efficient algorithm for the valid tree problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Solves the Valid Tree problem.

        Algorithm: Hash Table/Dictionary
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n) - linear scan plus hash operations
        Space Complexity: O(n) - store up to n elements
        """
        if not n:
            return True
        
        adjlist = {i: [] for i in range(n)}
        for n1, n2 in edges:  # Iterate through collection
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)

        visited = set()  # Mark node/element as visited
        def dfs(i, prevN):
            if i in visited:  # Mark node/element as visited
                return False
            
            visited.add(i)  # Mark node/element as visited

            for j in adjlist[i]:  # Iterate through collection
                if j == prevN:
                    continue
                
                if not dfs(j, i):
                    return False
                
            return True

        return dfs(0, -1) and len(visited) == n  # Mark node/element as visited
            


