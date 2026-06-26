# House Robber Solution
#
# This solution implements an efficient algorithm for the house robber problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Solves the House Robber problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        rob1, rob2 = 0, 0

        for n in nums:  # Iterate through collection
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        
        return rob2
