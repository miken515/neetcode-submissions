# Max Water Container Solution
#
# This solution implements an efficient algorithm for the max water container problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Solves the Max Water Container problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n) - linear scan of input
        Space Complexity: O(1) - minimal extra space used
        """
        
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:  # Iterate until condition fails
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return res
