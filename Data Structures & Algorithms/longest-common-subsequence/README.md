# Longest Common Subsequence

## Problem
Given two strings, find the length of the longest common subsequence (characters that appear in the same order, but not necessarily consecutive).

Example: `text1 = "abcde", text2 = "ace"` → `3` ("ace" is the LCS)

## Algorithm Explanation

### Approach: Dynamic Programming (Bottom-Up)
1. **Create** a 2D grid with dimensions (len(text1)+1) × (len(text2)+1)
2. **Fill** from bottom-right to top-left:
   - If characters match: `grid[i][j] = 1 + grid[i+1][j+1]` (diagonal)
   - If not: `grid[i][j] = max(grid[i+1][j], grid[i][j+1])` (take best of right or bottom)
3. **Return** `grid[0][0]` which contains the LCS length

### Time Complexity
- **O(m × n)** where m and n are lengths of the two strings

### Space Complexity
- **O(m × n)** for the DP grid

## Visual Representation

```
text1 = "ABE"
text2 = "DCE"

       ""  D  C  E
    "" 0   0  0  0
    A  0   0  0  0
    B  0   0  0  0
    E  0   0  0  1  ← Match at E, take diagonal + 1
    
Filled grid (bottom-up):
       ""  D  C  E
    "" 0   0  0  0
    A  0   0  0  0
    B  0   0  0  0
    E  0   0  0  1
    
Result: grid[0][0] = 1 (LCS length is "E")
```

## Key Insights
- DP avoids recalculating overlapping subproblems
- Grid rows represent text1, columns represent text2
- Diagonal move indicates character match
- Direction (right or bottom) is determined by maximum value
- Can be optimized to O(min(m,n)) space with rolling arrays
