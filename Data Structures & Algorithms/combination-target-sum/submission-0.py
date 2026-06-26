# Back tracking dfs
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Solves the Combination Target Sum problem.

        Algorithm: Stack-based
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n) - depends on problem constraints
        Space Complexity: O(n) - minimal extra space used
        """
        result = []

        def dfs(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            curr.pop()
            dfs(i+1, curr, total)

        
        dfs(0, [], 0)
        return result