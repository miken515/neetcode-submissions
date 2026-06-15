# Contains Duplicate

## Problem
Given an integer array, determine if any value appears more than once.

Example: `[1,2,3,1]` → `True`, `[1,2,3,4]` → `False`

## Algorithm Explanation

### Approach: HashSet
1. **Initialize** an empty set
2. **Iterate** through each number in the array
3. **Check** if number already exists in set:
   - If yes, return True (duplicate found)
   - If no, add it to the set
4. **Return** False if loop completes (no duplicates)

### Time Complexity
- **O(n)** where n is the length of the array

### Space Complexity
- **O(n)** for the hashset storage

## Visual Representation

```
Array: [1, 2, 3, 1]

Step 1: Check 1
  Set: {} → 1 not in set → Add 1
  Set: {1}

Step 2: Check 2
  Set: {1} → 2 not in set → Add 2
  Set: {1, 2}

Step 3: Check 3
  Set: {1, 2} → 3 not in set → Add 3
  Set: {1, 2, 3}

Step 4: Check 1 (again)
  Set: {1, 2, 3} → 1 IS in set → Return True ✓
```

## Key Insights
- HashSet provides O(1) average lookup time
- Early exit when duplicate is found (efficient)
- Simple and straightforward approach
- Space-efficient compared to sorting alternatives
