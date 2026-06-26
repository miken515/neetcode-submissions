# Find Minimum In Rotated Sorted Array Solution
#
# This solution implements an efficient algorithm for the find minimum in rotated sorted array problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Solves the Find Minimum In Rotated Sorted Array problem.

        Algorithm: Sorting
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n log n) - standard sorting complexity
        Space Complexity: O(1) or O(n) - depends on sorting algorithm
        """
        l = 0
        r = len(nums) - 1
        res = nums[l]
        while l <= r:  # Iterate until condition fails
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res
            
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1 #search right side
            else:
                r = mid - 1 #search left side

        return res                