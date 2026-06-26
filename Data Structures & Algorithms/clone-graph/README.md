# Clone Graph

## Problem

Given a reference to a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains a value and a list of neighbors.

Example:
- Input: Graph with 4 nodes
- Output: Deep copy of the entire graph

## Algorithm Explanation

### Approach: DFS/BFS with Hash Map

DFS/BFS with Hash Map - Use a hash map to track visited nodes and their clones.
For each node, recursively clone its neighbors. Handle cycles in the graph.

### Time Complexity
- **O(n + e) where n is nodes and e is edges**

### Space Complexity
- **O(n) for the hash map and recursion stack**

## Key Insights

- Understand the problem constraints and data structure options
- Consider trade-offs between time and space complexity
- Use appropriate data structures (arrays, hash sets, stacks, etc.)
- Handle edge cases properly
- Think through the algorithm before implementing

