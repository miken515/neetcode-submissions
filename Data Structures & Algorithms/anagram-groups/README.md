# Group Anagrams

## Problem
Given an array of strings, group anagrams together. Anagrams are words that contain the same letters but in a different order.

Example: `["eat","tea","ate","bat","ate"]` → `[["eat","tea","ate"],["bat"]]`

## Algorithm Explanation

### Approach: Character Count Signature
Two strings are anagrams if they have the exact same character frequencies. Instead of comparing strings directly, we can:

1. **Count character frequencies** for each string (using an array for letters a-z)
2. **Use the count as a key** in a hashmap (convert to tuple to make it hashable)
3. **Group strings** that have the same character count signature
4. **Return all groups**

### Time Complexity
- **O(n * k)** where n is the number of strings and k is the maximum length of a string

### Space Complexity
- **O(n * k)** to store all strings in the result

## Visual Representation

```
Input: ["eat", "tea", "ate", "bat", "ate"]

Step 1: Count characters for each string
  "eat" → [1,0,0,1,1,0,0,...] (a:1, e:1, t:1)
  "tea" → [1,0,0,1,1,0,0,...] (a:1, e:1, t:1) ← Same!
  "ate" → [1,0,0,1,1,0,0,...] (a:1, e:1, t:1) ← Same!
  "bat" → [1,0,1,0,0,1,0,...] (a:1, b:1, t:1) ← Different

Step 2: Group by signature
  Signature 1 → ["eat", "tea", "ate"]
  Signature 2 → ["bat"]

Output: [["eat", "tea", "ate"], ["bat"]]
```

## Key Insights
- Character frequency is the essence of anagrams
- Using a count array (fixed size 26) is more efficient than sorting
- Converting the count to a tuple makes it hashable for dictionary key use
