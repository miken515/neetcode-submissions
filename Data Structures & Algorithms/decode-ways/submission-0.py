# Decode Ways Solution
#
# This solution implements an efficient algorithm for the decode ways problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Solves the Decode Ways problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        prevprev = 0
        prev = 1
        cur = 0

        for i in range(len(s) - 1, -1, -1):  # Process each element
            if s[i] == "0":
                cur = 0
            else:
                cur = prev
            
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] < "7"):
                cur += prevprev
            
            prevprev = prev
            prev = cur
        return cur