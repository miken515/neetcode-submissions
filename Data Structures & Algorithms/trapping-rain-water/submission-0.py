# Trapping Rain Water Solution
#
# This solution implements an efficient algorithm for the trapping rain water problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Solves the Trapping Rain Water problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n) - linear scan of input
        Space Complexity: O(1) - minimal extra space used
        """
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        res = 0

        while l < r:  # Iterate until condition fails
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]
        
        return res

