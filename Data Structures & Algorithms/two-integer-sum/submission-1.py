class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Solves the Two Integer Sum problem.

        Algorithm: Hash Table/Dictionary
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n) - linear scan plus hash operations
        Space Complexity: O(n) - store up to n elements
        """
        # create map
        previousMap = {}

        for i, n in enumerate(nums):  # Iterate through collection
            print('Previous Map:', previousMap)
            print('I,N', i, n)
            difference = target - n
            print('Target', target)
            print('Diff', difference)
            if difference in previousMap:
                return[previousMap[difference], i]
            previousMap[n] = i 
        return

# Create a map, enumerate, then it finds the difference, using that difference in the map, 
# If difference is not found in the map, we add the first num from the list to the mapp
# Window problem