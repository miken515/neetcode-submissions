# Validate Parentheses Solution
#
# This solution implements an efficient algorithm for the validate parentheses problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Solves the Validate Parentheses problem.

        Algorithm: Stack-based
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n) - depends on problem constraints
        Space Complexity: O(n) - minimal extra space used
        """
        stack = []
        map = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s:   # Iterate through collection
            if c in map:
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False