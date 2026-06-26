# Coin Change Solution
#
# This solution implements an efficient algorithm for the coin change problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Solves the Coin Change problem.

        Algorithm: Dynamic Programming
        - Approach: Build solution bottom-up using subproblems
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n) - compute each subproblem once
        Space Complexity: O(n) - store results for each subproblem
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        print(dp)
        for a in range(1, amount + 1):  # Process each element
            for c in coins:  # Iterate through collection
                print('coin:', c)
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1