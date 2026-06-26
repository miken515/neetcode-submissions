# Missing Number Solution
#
# This solution implements an efficient algorithm for the missing number problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Solves the Missing Number problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        res = len(nums)

        for i in range(len(nums)):  # Process each element
            res += i - nums[i]
        return res