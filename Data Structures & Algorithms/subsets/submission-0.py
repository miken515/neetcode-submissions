# Subsets Solution
#
# This solution implements an efficient algorithm for the subsets problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Solves the Subsets problem.

        Algorithm: Stack-based
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n) - depends on problem constraints
        Space Complexity: O(n) - minimal extra space used
        """
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res