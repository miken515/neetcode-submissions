# Valid Anagram

## Problem
Given two strings, determine if one is an anagram of the other. An anagram contains the same characters with the same frequencies.

Example: `s = "anagram", t = "nagaram"` → `True`

## Algorithm Explanation

### Approach: Sorting
1. **Sort** both strings
2. **Compare** the sorted versions
3. If sorted strings are equal, they're anagrams

### Time Complexity
- **O(n log n)** where n is the length of the string (due to sorting)

### Space Complexity
- **O(1)** or **O(n)** depending on sorting algorithm

## Visual Representation

```
s = "anagram"
t = "nagaram"

Step 1: Sort both strings
  s sorted: "aaagmnr"
  t sorted: "aaagmnr"

Step 2: Compare
  "aaagmnr" == "aaagmnr" → True ✓

Example of non-anagram:
  s = "rat"
  t = "car"
  
  s sorted: "art"
  t sorted: "acr"
  
  "art" != "acr" → False ✗
```

## Key Insights
- Simple and elegant solution
- Relies on Python's built-in sorted() function
- Works because anagrams have identical characters when sorted
- Less efficient than counting approach for very long strings
