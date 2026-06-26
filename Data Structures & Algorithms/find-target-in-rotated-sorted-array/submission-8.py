# Find Target In Rotated Sorted Array Solution
#
# This solution implements an efficient algorithm for the find target in rotated sorted array problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Solves the Find Target In Rotated Sorted Array problem.

        Algorithm: Sorting
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n log n) - standard sorting complexity
        Space Complexity: O(1) or O(n) - depends on sorting algorithm
        """
        low = 0
        high = len(nums) - 1
 
        while low <= high:  # Iterate until condition fails
            mid = (low + high) // 2
    
            # Target found
            if target == nums[mid]:
                return mid
            
            # Left half is sorted (no rotation in this half)
            if nums[low] <= nums[mid]:
                # Target is outside the sorted left half — search right
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                # Target is within the sorted left half — search left
                else:
                    high = mid - 1
            
            # Right half is sorted (rotation point is in left half)
            else:
                # Target is outside the sorted right half — search left
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                # Target is within the sorted right half — search right
                else:
                    low = mid + 1
    
        # Target not found
        return -1