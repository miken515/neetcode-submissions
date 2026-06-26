# Eating Bananas Solution
#
# This solution implements an efficient algorithm for the eating bananas problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Solves the Eating Bananas problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        low, high = 1, max(piles)
        res = high
        
        while low <= high:  # Iterate until condition fails
            k = (high + low) // 2
            totalTime = 0

            for p in piles:  # Iterate through collection
                totalTime += math.ceil(float(p) / k)
            
            if totalTime <= h:
                res = k
                high = k - 1
            else:
                low = k + 1
        
        return res
