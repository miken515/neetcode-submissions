# Maximum Subarray Solution
#
# This solution implements an efficient algorithm for the maximum subarray problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Solves the Maximum Subarray problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        maxSum = nums[0]
        curSum = 0

        for n in nums:  # Iterate through collection
            curSum = max(curSum, 0) + n
            maxSum = max(curSum, maxSum)
        return maxSum