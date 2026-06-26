# Longest Consecutive Sequence

## Problem

Given an unsorted array of integers, find the length of the longest consecutive sequence.

You must write an algorithm that runs in O(n) time complexity.

Example:
- Input: [100, 4, 200, 1, 3, 2]
- Output: 4 (the sequence is [1, 2, 3, 4])

## Algorithm Explanation

### Approach: Hash Set

Hash Set - Convert array to set for O(1) lookups.
For each number, only start counting if it's the beginning of a sequence.
Count consecutive numbers by checking if next number exists in set.

### Time Complexity
- **O(n) - convert to set and iterate through numbers**

### Space Complexity
- **O(n) - hash set to store all numbers**

## Key Insights

- Understand the problem constraints and data structure options
- Consider trade-offs between time and space complexity
- Use appropriate data structures (arrays, hash sets, stacks, etc.)
- Handle edge cases properly
- Think through the algorithm before implementing

