# House Robber Ii Solution
#
# This solution implements an efficient algorithm for the house robber ii problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Solves the House Robber Ii problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        maxRob = max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        return maxRob
    
    def helper(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:  # Iterate through collection
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2