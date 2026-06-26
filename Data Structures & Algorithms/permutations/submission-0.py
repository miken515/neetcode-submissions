# Permutations Solution
#
# This solution implements an efficient algorithm for the permutations problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Solves the Permutations problem.

        Algorithm: Backtracking
        - Approach: Explore all possibilities with pruning
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(2^n) - exponential search space
        Space Complexity: O(n) - recursion depth and result storage
        """

        self.res = []
        self.backtrack(nums, 0)
        return self.res
        
    def backtrack(self, nums: List[int], indx: int):
        if indx == len(nums):
            self.res.append(nums[:])
            return
        for i in range(indx, len(nums)):  # Process each element
            nums[indx], nums[i] = nums[i], nums[indx]
            self.backtrack(nums, indx + 1)
            nums[indx], nums[i] = nums[i], nums[indx]