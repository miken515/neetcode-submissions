# String Encode And Decode Solution
#
# This solution implements an efficient algorithm for the string encode and decode problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Solves the String Encode And Decode problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        res = ""
        for s in strs:  # Iterate through collection
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):  # Iterate until condition fails
            j = i
            while s[j] != '#':  # Iterate until condition fails
                j += 1

            length = int(s[i:j]) #starts from i, and goes up to j

            res.append(s[j + 1 : j + 1 + length]) # j + 1, is the first char after delimiter
            i = j + 1 + length # make i start at the next work
        return res

