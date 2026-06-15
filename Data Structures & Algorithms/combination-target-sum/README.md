# Combination Sum

## Problem
Given an array of distinct integers and a target number, find all unique combinations of candidates where the sum equals the target. The same number may be used multiple times.

Example: `candidates = [2,3,6,7], target = 7` → `[[2,2,3],[7]]`

## Algorithm Explanation

### Approach: Backtracking (DFS with Recursion)
1. **Base cases**:
   - If current sum equals target, add combination to result
   - If we've used all candidates or sum exceeds target, backtrack
2. **Two choices for each number**:
   - **Include** it: Add to current combination and recurse with same index
   - **Exclude** it: Remove from combination and recurse with next index
3. **Backtrack** by removing the last element before trying the exclude branch

### Time Complexity
- **O(2^(T/M))** where T is target and M is minimum candidate value

### Space Complexity
- **O(T/M)** for recursion call stack depth

## Visual Representation

```
Candidates: [2,3,6,7], Target: 7

                    []
                   /  |  \  \
                  /   |   \  \
              [2]   [3]   [6] [7]
             / |     / |     \
          [2,2] [2,3] [3] [3,3] [6,7]✗
          / |
      [2,2,2] [2,2,3]✓
      
Legend:
  ✓ = Valid solution (sum = 7)
  ✗ = Prune (sum > 7)

Result: [[2,2,3], [7]]
```

## Key Insights
- Backtracking explores all possible combinations efficiently
- Reusing the same index allows unlimited repetitions of a number
- Pruning (checking if total > target) reduces unnecessary exploration
- Copy combinations when adding to result (curr.copy())
