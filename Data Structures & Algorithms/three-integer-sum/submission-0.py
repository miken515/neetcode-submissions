# Three Integer Sum Solution
#
# This solution implements an efficient algorithm for the three integer sum problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Solves the Three Integer Sum problem.

        Algorithm: Sorting
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n log n) - standard sorting complexity
        Space Complexity: O(1) or O(n) - depends on sorting algorithm
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):  # Iterate through collection
            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:  # Iterate until condition fails
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else: 
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # removing dupes from l side
                    while nums[l] == nums[l - 1] and l < r:  # Iterate until condition fails
                        l += 1

        return res