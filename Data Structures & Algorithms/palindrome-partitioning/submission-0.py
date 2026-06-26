# Palindrome Partitioning Solution
#
# This solution implements an efficient algorithm for the palindrome partitioning problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Solves the Palindrome Partitioning problem.

        Algorithm: Backtracking
        - Approach: Explore all possibilities with pruning
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(2^n) - exponential search space
        Space Complexity: O(n) - recursion depth and result storage
        """
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):  # Process each element
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        result = []
        backtrack(0, [])
        return result
