# Longest Repeating Substring With Replacement Solution
#
# This solution implements an efficient algorithm for the longest repeating substring with replacement problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Solves the Longest Repeating Substring With Replacement problem.

        Algorithm: Hash Table/Dictionary
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n) - linear scan plus hash operations
        Space Complexity: O(n) - store up to n elements
        """
        map = {}
        l, r = 0, 0
        res = 0
        maxFreq = 0

        while l <= r < len(s):  # Iterate until condition fails
            char = s[r]

            if char not in map:
                map[char] = 1
            else:
                map[char] += 1

            maxFreq = max(maxFreq, map[char])

            while r - l + 1 - maxFreq > k:  # Iterate until condition fails
                map[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        return res