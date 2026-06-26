# Binary Tree Diameter

## Problem

Find the length of the diameter of the binary tree.

The diameter of a binary tree is the length of the longest path between any two nodes.
The path may or may not pass through the root.

Example:
- Input: Binary tree with root 1, left child 2, right child 3
- Output: 3 (path: 2 -> 1 -> 3)

## Algorithm Explanation

### Approach: DFS (Depth-First Search)

DFS (Depth-First Search) - For each node, calculate the maximum depth of left and right subtrees. 
The diameter at each node is the sum of left depth + right depth.
Track the maximum diameter seen so far.

### Time Complexity
- **O(n) where n is the number of nodes**

### Space Complexity
- **O(h) where h is the height of the tree (recursion stack)**

## Key Insights

- Understand the problem constraints and data structure options
- Consider trade-offs between time and space complexity
- Use appropriate data structures (arrays, hash sets, stacks, etc.)
- Handle edge cases properly
- Think through the algorithm before implementing

