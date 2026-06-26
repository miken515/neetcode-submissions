# Palindromic Substrings Solution
#
# This solution implements an efficient algorithm for the palindromic substrings problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Solves the Palindromic Substrings problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        res = 0

        for i in range(len(s)):  # Process each element
            #Odd length of s
            res += self.countPali(s, i, i)
            
            # evn length
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:  # Iterate until condition fails
            res += 1
            l -= 1
            r += 1
        return res