# Jump Game Solution
#
# This solution implements an efficient algorithm for the jump game problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Solves the Jump Game problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        n = len(nums)
        maxJump = 0

        for i in range(n):  # Process each element
            if i > maxJump:
                return False
            
            maxJump = max(maxJump, i + nums[i])

            if maxJump >= n - 1:
                return True
        
        return True