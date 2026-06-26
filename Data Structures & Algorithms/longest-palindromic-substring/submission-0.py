# Longest Palindromic Substring Solution
#
# This solution implements an efficient algorithm for the longest palindromic substring problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Solves the Longest Palindromic Substring problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        result = ''
        resultLength = 0

        for i in range(len(s)):  # Process each element
            #odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:  # Iterate until condition fails
                if (r - l + 1) > resultLength:
                    result = s[l:r+1]
                    resultLength = r - l + 1
                    
                l -= 1
                r += 1

            #even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:  # Iterate until condition fails
                if (r - l + 1) > resultLength:
                    result = s[l:r+1]
                    resultLength = r - l + 1
                    
                l -= 1
                r += 1

        return result

