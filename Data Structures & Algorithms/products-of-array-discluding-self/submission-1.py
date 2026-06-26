# Products Of Array Discluding Self Solution
#
# This solution implements an efficient algorithm for the products of array discluding self problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Solves the Products Of Array Discluding Self problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        n = len(nums)
        res = [1] * len(nums)
        prefix = 1
        postfix = 1

        for i in range(n):  # Process each element
            res[i] = prefix
            prefix *= nums[i]


        for i in range(n - 1, -1, -1):  # Process each element
            res[i] *= postfix
            postfix *= nums[i]

        return res