# Longest Palindromic Substring

## Problem
Given a string, find the longest palindromic substring. A palindrome reads the same forwards and backwards.

Example: `s = "bbbab"` → `"bbb"`

## Algorithm Explanation

### Approach: Expand Around Center
1. **For each position** in the string:
   - **Treat it as center** for odd-length palindrome (left=right=i)
   - **Treat it as center** for even-length palindrome (left=i, right=i+1)
2. **Expand** left and right pointers while characters match
3. **Track** the longest palindrome found
4. **Return** the longest palindrome string

### Time Complexity
- **O(n²)** where n is the length of the string

### Space Complexity
- **O(1)** if not counting output; O(n) for result storage

## Visual Representation

```
String: "bbbab"
Positions: 0 1 2 3 4

Center at index 1 (odd length):
  "bbbab"
    ^  (center)
   / \
  L   R expand → "bbb" (length 3)

Center at index 2 (odd length):
  "bbbab"
      ^ (center)
     / \
    L   R → "b" (length 1)

Center at index 3 (even length):
  "bbbab"
       ^^(L=3, R=4) → "ab" doesn't match

Best palindrome found: "bbb" (length 3)

Expansion process:
  Start: (L,R) = (1,1) = "b"
  Expand: (L,R) = (0,2) = "bbb" ✓
  Expand: (L,R) = (-1,3) = out of bounds or mismatch ✗
```

## Key Insights
- Center expansion is efficient for this problem
- Handles both odd-length (single center) and even-length (between two chars) palindromes
- Early termination when characters don't match
- Better than brute force or DP for most practical cases
