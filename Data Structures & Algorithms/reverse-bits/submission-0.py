# Reverse Bits Solution
#
# This solution implements an efficient algorithm for the reverse bits problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Solves the Reverse Bits problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        res = 0
        for i in range(32):  # Process each element
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res