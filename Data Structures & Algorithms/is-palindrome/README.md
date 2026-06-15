# Valid Palindrome

## Problem
Given a string, determine if it is a valid palindrome, considering only alphanumeric characters and ignoring case.

Example: `s = "A man, a plan, a canal: Panama"` → `True`

## Algorithm Explanation

### Approach: Filter and Reverse
1. **Filter** the string to keep only alphanumeric characters
2. **Convert** all characters to lowercase
3. **Compare** the filtered string with its reverse
4. If they match, it's a palindrome

### Time Complexity
- **O(n)** where n is the length of the string

### Space Complexity
- **O(n)** for the new filtered string

## Visual Representation

```
Input: "A man, a plan, a canal: Panama"

Step 1: Filter alphanumeric and lowercase
  "A man, a plan, a canal: Panama"
  ↓ (remove non-alphanumeric, lowercase)
  "amanaplanacanalpanama"

Step 2: Create reverse
  Original: "amanaplanacanalpanama"
  Reverse:  "amanaplanacanalpanama"
  
Step 3: Compare
  "amanaplanacanalpanama" == "amanaplanacanalpanama" → True ✓

Non-palindrome example:
  Input: "hello"
  Filtered: "hello"
  Reverse: "olleh"
  "hello" != "olleh" → False ✗
```

## Key Insights
- Filtering ensures we only compare meaningful characters
- Case-insensitive comparison handles uppercase/lowercase
- Simple reverse comparison is efficient and clear
- String slicing `[::-1]` is Pythonic way to reverse
