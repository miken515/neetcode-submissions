# Longest Consecutive Sequence Solution
#
# This solution implements an efficient algorithm for the longest consecutive sequence problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Solves the Longest Consecutive Sequence problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        numSet = set(nums)
        print(numSet)
        longest = 0

        for n in nums:  # Iterate through collection
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:  # Iterate until condition fails
                    length += 1
                longest = max(length, longest)
        
        return longest