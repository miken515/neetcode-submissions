# Is Anagram Solution
#
# This solution implements an efficient algorithm for the is anagram problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Solves the Is Anagram problem.

        Algorithm: Sorting
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n log n) - standard sorting complexity
        Space Complexity: O(1) or O(n) - depends on sorting algorithm
        """
        return sorted(s) == sorted(t)