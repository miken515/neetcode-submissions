#$ Hashmap btw
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Solves the Duplicate Integer problem.

        Algorithm: Hash Table/Dictionary
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n) - linear scan plus hash operations
        Space Complexity: O(n) - store up to n elements
        """
        hashset = set()

        for n in nums:  # Iterate through collection
            if n in hashset:
                return True
            hashset.add(n)
        return False
