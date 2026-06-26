class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Solves the Top K Elements In List problem.

        Algorithm: Hash Table/Dictionary
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n) - linear scan plus hash operations
        Space Complexity: O(n) - store up to n elements
        """
        # Hashmap
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:  # Iterate through collection
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():  # Iterate through collection
            freq[c].append(n) # for this n, it appears c times

        res = []

        for i in range(len(freq) - 1, 0, -1):  # Process each element
            for n in freq[i]:  # Iterate through collection
                res.append(n)
                if len(res) == k:
                    return res
        




