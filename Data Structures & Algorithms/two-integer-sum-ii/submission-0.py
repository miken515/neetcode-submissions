# Two Integer Sum Ii Solution
#
# This solution implements an efficient algorithm for the two integer sum ii problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Solves the Two Integer Sum Ii problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n) - linear scan of input
        Space Complexity: O(1) - minimal extra space used
        """
        l, r = 0, len(numbers) - 1

        while l < r:  # Iterate until condition fails
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l +1, r + 1]
        return []