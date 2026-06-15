# Reorder List

## Problem
Given a linked list, reorder it as: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

Example: `1 → 2 → 3 → 4 → 5` → `1 → 5 → 2 → 4 → 3`

## Algorithm Explanation

### Approach: Three-Step Process
1. **Find Middle** using slow/fast pointers
   - Slow moves 1 step, fast moves 2 steps
   - When fast reaches end, slow is at middle
2. **Reverse Second Half**
   - Reverse the linked list from middle to end
3. **Merge** the two halves alternately
   - Interleave nodes from first half and reversed second half

### Time Complexity
- **O(n)** where n is the length of the list

### Space Complexity
- **O(1)** - only constant extra space

## Visual Representation

```
Original: 1 → 2 → 3 → 4 → 5

Step 1: Find middle with slow/fast pointers
  Slow: 1 → 2 → 3 (stops here)
  Fast: 1 → 3 → 5 (reaches end)
  Middle found: node 3

Step 2: Reverse second half (3 → 4 → 5 becomes 5 → 4 → 3)
  First half:  1 → 2 → 3
  Second half: 5 → 4 → None (None ← 4 ← 5)
  
Step 3: Merge alternately
  first = 1,  second = 5
  1 → 5 → 2 → 4 → 3
  
  Detailed merge:
  1.next = 5    → 1 → 5 → ...
  5.next = 2    → 1 → 5 → 2 → ...
  2.next = 4    → 1 → 5 → 2 → 4 → ...
  4.next = 3    → 1 → 5 → 2 → 4 → 3 → ...
  3.next = None → 1 → 5 → 2 → 4 → 3

Result: 1 → 5 → 2 → 4 → 3
```

## Key Insights
- Slow/fast pointer technique finds middle in single pass
- Reversing is done in-place by changing pointers
- Merging requires careful pointer manipulation to maintain both lists
- No extra space needed (not counting output)
