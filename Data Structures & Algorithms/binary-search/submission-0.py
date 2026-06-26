# Binary Search Solution
#
# This solution implements an efficient algorithm for the binary search problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Solves the Binary Search problem.

        Algorithm: Binary Search
        - Approach: Divide search space in half each iteration
        - Key Operations: iterate through input with conditions

        Time Complexity: O(log n) - halve search space each iteration
        Space Complexity: O(1) - iterative approach uses constant space
        """
        low, high = 0, len(nums) - 1

        while low <= high:  # Iterate until condition fails
            mid = low + (high - low) // 2

            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1 
            else:
                return mid

        return -1 