# recursive
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Solves the Climbing Stairs problem.

        Algorithm: Backtracking
        - Approach: Explore all possibilities with pruning
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(2^n) - exponential search space
        Space Complexity: O(n) - recursion depth and result storage
        """
        one = 1
        two = 1
        for i in range(n - 1):  # Process each element
            tmp = one
            one = one + two
            two = tmp
        return one