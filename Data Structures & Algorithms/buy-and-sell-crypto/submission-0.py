# sliding window
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Solves the Buy And Sell Crypto problem.

        Algorithm: Sliding Window
        - Approach: Maintain window of relevant elements
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n) - window slides through array once
        Space Complexity: O(k) - store elements in window
        """
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):  # Iterate until condition fails
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
                
            r += 1

        return maxProfit