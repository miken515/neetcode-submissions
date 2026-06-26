# Is Palindrome Solution
#
# This solution implements an efficient algorithm for the is palindrome problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Solves the Is Palindrome problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        newStr = ''

        for c in s:  # Iterate through collection
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]