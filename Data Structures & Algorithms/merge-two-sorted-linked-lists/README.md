# Merge Two Sorted Lists

## Problem
Given two sorted linked lists, merge them into one sorted linked list.

Example: `list1 = [1,2,4], list2 = [1,3,4]` → `[1,1,2,3,4,4]`

## Algorithm Explanation

### Approach: Two-Pointer Merge
1. **Handle edge cases**: If either list is empty, return the other
2. **Create dummy node** to simplify logic (avoid special-casing head)
3. **Compare values** at current positions in both lists
4. **Attach smaller node** to the result and advance that pointer
5. **Attach remaining nodes** from whichever list has elements left
6. **Return** dummy.next (the actual merged list head)

### Time Complexity
- **O(n + m)** where n and m are lengths of the two lists

### Space Complexity
- **O(1)** - only a constant amount of extra space (reuses existing nodes)

## Visual Representation

```
list1 = 1 → 2 → 4 → None
list2 = 1 → 3 → 4 → None

Step 1: Create dummy node
  dummy → None
  builder points to dummy

Step 2: Compare and merge
  Compare: 1 vs 1 → attach 1 (from list1), advance builder and list1
  dummy → 1 → None
  
  Compare: 2 vs 1 → attach 1 (from list2), advance builder and list2
  dummy → 1 → 1 → None
  
  Compare: 2 vs 3 → attach 2 (from list1), advance builder and list1
  dummy → 1 → 1 → 2 → None
  
  Compare: 4 vs 3 → attach 3 (from list2), advance builder and list2
  dummy → 1 → 1 → 2 → 3 → None
  
  Compare: 4 vs 4 → attach 4 (from list1), advance builder and list1
  dummy → 1 → 1 → 2 → 3 → 4 → None
  
  list1 exhausted, attach remaining list2
  dummy → 1 → 1 → 2 → 3 → 4 → 4 → None

Result: dummy.next = 1 → 1 → 2 → 3 → 4 → 4 → None
```

## Key Insights
- Dummy node simplifies implementation (no special head handling)
- In-place merge reuses nodes (space-efficient)
- Always move the pointer of the list from which we took a node
- Handle remaining nodes at the end (one list will be exhausted first)
