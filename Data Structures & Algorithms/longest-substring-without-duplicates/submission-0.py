# Longest Substring Without Duplicates Solution
#
# This solution implements an efficient algorithm for the longest substring without duplicates problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Solves the Longest Substring Without Duplicates problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        charSet = set()
        left = 0
        res = 0
        for right in range(len(s)):  # Process each element
            while s[right] in charSet:  # Iterate until condition fails
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            res = max (res, right - left + 1)

        return res