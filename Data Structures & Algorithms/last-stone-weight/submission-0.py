# Last Stone Weight Solution
#
# This solution implements an efficient algorithm for the last stone weight problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Solves the Last Stone Weight problem.

        Algorithm: Stack-based
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n) - depends on problem constraints
        Space Complexity: O(n) - minimal extra space used
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:  # Iterate until condition fails
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                print(first - second)
                heapq.heappush(stones, first - second)
            
        stones.append(0)
        return abs(stones[0])
