# Course Schedule Solution
#
# This solution implements an efficient algorithm for the course schedule problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Solves the Course Schedule problem.

        Algorithm: Hash Table/Dictionary
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n) - linear scan plus hash operations
        Space Complexity: O(n) - store up to n elements
        """
        preMap = {i: [] for i in range(numCourses)}
        for i, pre in prerequisites:  # Iterate through collection
            print(i, pre)
            preMap[i].append(pre)
        
        visited = set()  # Mark node/element as visited

        def dfs(crs):
            if crs in visited:  # Mark node/element as visited
                return False
            
            if preMap[crs] == []:
                return True

            visited.add(crs)  # Mark node/element as visited

            for pre in preMap[crs]:  # Iterate through collection
                if not dfs(pre):
                    return False
            
            visited.remove(crs)  # Mark node/element as visited
            preMap[crs] = []
            return True
        
        for c in range(numCourses):  # Process each element
            if not dfs(c):
                return False
        return True