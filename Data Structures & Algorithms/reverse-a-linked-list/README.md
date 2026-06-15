# Reverse Linked List

## Problem
Given a linked list, reverse it (both iteratively and recursively).

Example: `1 → 2 → 3 → 4` → `4 → 3 → 2 → 1`

## Algorithm Explanation (Recursive Approach)

### Approach: Recursion with Pointer Reversal
1. **Base case**: If list is empty, return None
2. **Recursive case**:
   - Find the new head by recursing to the end
   - Once at the end, reverse the pointer: `head.next.next = head`
   - Set current node's next to None
3. **Return** the new head (found during recursion)

### Time Complexity
- **O(n)** where n is the length of the list

### Space Complexity
- **O(n)** for recursion call stack

## Visual Representation

```
Original: 1 → 2 → 3 → 4

Recursive calls (going down):
  reverseList(1)
    reverseList(2)
      reverseList(3)
        reverseList(4)
          reverseList(None) → returns None (base case)
        
Reversing (coming back up):
  At node 4: newHead = 4 (head of reversed part)
  At node 3: 3.next.next = 3 (make 4 → 3)
             3.next = None
             Return 4
             
             Before: ... → 3 → 4
             After:  ... → 3 ← 4  (reversed!)
             
  At node 2: 2.next.next = 2 (make 3 → 2)
             2.next = None
             Return 4
             
  At node 1: 1.next.next = 1 (make 2 → 1)
             1.next = None
             Return 4

Final: 4 → 3 → 2 → 1

Pointer reversal at each step:
  head = 3, head.next = 4
  head.next.next = head → 4.next = 3 (changes 4 → None to 4 → 3)
  head.next = None (breaks old link 3 → 4)
```

## Key Insights
- Recursive approach is elegant but uses O(n) stack space
- Key operation: `head.next.next = head` reverses a single link
- Must set `head.next = None` to break the old forward link
- New head is found at the deepest recursion level
- Iterative approach exists (uses O(1) space) but recursive is shown here
