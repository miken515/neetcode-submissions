# Valid Parentheses

## Problem
Given a string with brackets, determine if they are valid (every opening bracket has a matching closing bracket in the correct order).

Example: `s = "({[]})"` → `True`, `s = "(]"` → `False`

## Algorithm Explanation

### Approach: Stack with Hashmap
1. **Create a map** of closing brackets to their matching opening brackets
2. **Iterate** through each character:
   - If it's a **closing bracket**:
     - Check if stack is empty or top doesn't match → return False
     - Otherwise pop from stack
   - If it's an **opening bracket**: push to stack
3. **Return** True if stack is empty at end (all matched)

### Time Complexity
- **O(n)** where n is the length of the string

### Space Complexity
- **O(n)** for the stack (worst case all opening brackets)

## Visual Representation

```
String: "({[]})"

Bracket map:
  ')' → '('
  ']' → '['
  '}' → '{'

Processing:
  '(' : not in map → push to stack
    Stack: ['(']
    
  '{' : not in map → push to stack
    Stack: ['(', '{']
    
  '[' : not in map → push to stack
    Stack: ['(', '{', '[']
    
  ']' : in map, map[']'] = '['
    stack[-1] = '[' → matches!
    Pop from stack
    Stack: ['(', '{']
    
  '}' : in map, map['}'] = '{'
    stack[-1] = '{' → matches!
    Pop from stack
    Stack: ['(']
    
  ')' : in map, map[')'] = '('
    stack[-1] = '(' → matches!
    Pop from stack
    Stack: []

Final: Stack is empty → Valid! ✓

Invalid example: "({)}"
  After processing '(', '{'
  Stack: ['(', '{']
  
  See ')': map[')'] = '('
  But stack[-1] = '{' ≠ '('
  Return False ✗
```

## Key Insights
- Stack naturally handles nested structures
- Closing bracket mapping eliminates multiple conditionals
- Stack order matters: most recent opening bracket should match current closing bracket
- Empty stack at end ensures all brackets are matched
- Works for any number and type of bracket pairs
