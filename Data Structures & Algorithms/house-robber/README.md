# House Robber

## Problem

You are a robber planning to rob houses along a street.
Each house has a certain amount of money stashed. Adjacent houses cannot be robbed.
Return the maximum amount of money you can rob without alerting the police.

Example:
- Input: [1, 2, 3, 1]
- Output: 4 (rob house 0 and 2: 1 + 3 = 4)

## Algorithm Explanation

### Approach: Dynamic Programming

Dynamic Programming - For each house, decide to rob it or skip it.
dp[i] = maximum money from houses 0 to i
dp[i] = max(dp[i-1], dp[i-2] + house[i])

### Time Complexity
- **O(n) - process each house once**

### Space Complexity
- **O(1) - only track previous values**

## Key Insights

- Understand the problem constraints and data structure options
- Consider trade-offs between time and space complexity
- Use appropriate data structures (arrays, hash sets, stacks, etc.)
- Handle edge cases properly
- Think through the algorithm before implementing

