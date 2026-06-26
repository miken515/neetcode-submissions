# Find Duplicate Integer Solution
#
# This solution implements an efficient algorithm for the find duplicate integer problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Solves the Find Duplicate Integer problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n) - linear scan of input
        Space Complexity: O(1) - minimal extra space used
        """
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:  # Iterate until condition fails
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        slow = 0

        while slow != fast:  # Iterate until condition fails
            slow = nums[slow]
            fast = nums[fast]

        return slow

