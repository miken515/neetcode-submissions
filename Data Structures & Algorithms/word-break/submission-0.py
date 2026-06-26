# Word Break Solution
#
# This solution implements an efficient algorithm for the word break problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Solves the Word Break problem.

        Algorithm: Dynamic Programming
        - Approach: Build solution bottom-up using subproblems
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n) - compute each subproblem once
        Space Complexity: O(n) - store results for each subproblem
        """
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):  # Process each element
            for word in wordDict:  # Iterate through collection
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]

                if dp[i]:
                    break
        
        return dp[0]

