# Longest Increasing Subsequence Solution
#
# This solution implements an efficient algorithm for the longest increasing subsequence problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Solves the Longest Increasing Subsequence problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        ls = [1] * len(nums)


        for i in range(len(nums) -1, -1, -1):  # Process each element
            for j in range(i + 1, len(nums)):  # Process each element
                if nums[i] < nums[j]:
                    ls[i] = max(ls[i], 1 + ls[j])
        
        return max(ls)
