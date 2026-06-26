# Number Of One Bits Solution
#
# This solution implements an efficient algorithm for the number of one bits problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Solves the Number Of One Bits problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n) - linear scan of input
        Space Complexity: O(1) - minimal extra space used
        """
        count = 0

        while n:  # Iterate until condition fails
            count += n % 2
            n = n >> 1
        return count