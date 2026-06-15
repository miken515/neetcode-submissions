# Two Sum

## Problem
Given an array of integers and a target, find the indices of the two numbers that add up to the target. You may assume each input has exactly one solution.

Example: `nums = [2,7,11,15], target = 9` → `[0,1]` (2 + 7 = 9)

## Algorithm Explanation

### Approach: Hash Map (One-Pass)
1. **Initialize** an empty hashmap
2. **For each number** in the array:
   - Calculate the complement: `difference = target - num`
   - **Check** if difference exists in the map:
     - If yes, return indices of both numbers
     - If no, add current number to map with its index
3. **Continue** until solution is found

### Time Complexity
- **O(n)** where n is the length of the array

### Space Complexity
- **O(n)** for the hashmap storage

## Visual Representation

```
nums = [2, 7, 11, 15], target = 9

Iteration 1 (num = 2, index = 0):
  difference = 9 - 2 = 7
  Is 7 in map? No
  Add to map: {2: 0}
  
Iteration 2 (num = 7, index = 1):
  difference = 9 - 7 = 2
  Is 2 in map? Yes! (at index 0)
  Return [0, 1] ✓

Explanation:
  We stored 2 at index 0
  When we see 7, we know 2 + 7 = 9
  So indices [0, 1] is our answer

Why this works:
  target = num1 + num2
  num2 = target - num1
  
  If we've seen num2 before, we found our pair!
```

## Key Insights
- Hash map allows O(1) lookups of needed complement
- Single pass through array (no sorting needed)
- Store numbers as we iterate so complements can be found
- Works because we need to find exactly one pair
- More efficient than two-pointer or brute force approaches
