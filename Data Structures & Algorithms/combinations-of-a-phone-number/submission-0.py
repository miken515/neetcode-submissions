# Combinations Of A Phone Number Solution
#
# This solution implements an efficient algorithm for the combinations of a phone number problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Solves the Combinations Of A Phone Number problem.

        Algorithm: Backtracking
        - Approach: Explore all possibilities with pruning
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(2^n) - exponential search space
        Space Complexity: O(n) - recursion depth and result storage
        """
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):

            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digitToChar[digits[i]]:  # Iterate through collection
                backtrack(i + 1, curStr + c)
        
        if digits:
            backtrack(0, "")
        
        return res

