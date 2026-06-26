# Hashmap problem
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Solves the Anagram Groups problem.

        Algorithm: Hash Table/Dictionary
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n) - linear scan plus hash operations
        Space Complexity: O(n) - store up to n elements
        """
        # Use defaultdict to group anagrams by their character count signature
        result = defaultdict(list)

        # Process each string in the input list
        for s in strs:  # Iterate through collection
            # Create a count array for letters a-z (26 total)
            count = [0] * 26  # a-z chars

            # Count frequency of each character
            for c in s:  # Iterate through collection
                count[ord(c) - ord('a')] += 1

            # Use the count array as a key (convert to tuple for hashability)
            # All anagrams will have the same count signature
            result[tuple(count)].append(s)

        # Return all grouped anagrams as a list
        return list(result.values())
