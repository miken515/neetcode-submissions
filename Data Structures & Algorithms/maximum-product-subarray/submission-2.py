# Maximum Product Subarray Solution
#
# This solution implements an efficient algorithm for the maximum product subarray problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Solves the Maximum Product Subarray problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:  # Iterate through collection
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res