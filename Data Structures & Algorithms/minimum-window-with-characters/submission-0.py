# Minimum Window With Characters Solution
#
# This solution implements an efficient algorithm for the minimum window with characters problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Solves the Minimum Window With Characters problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: iterate through input with conditions

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        res = ""
        l = 0
        count = Counter(t)
        window = Counter()
        print(count)
        print(window)

        for i in range(len(s)):  # Process each element
            window[s[i]] += 1
            if window >= count:
                while window[s[l]] > count[s[l]]:  # Iterate until condition fails
                    window[s[l]] -= 1
                    l += 1
                
                if not res or (i - l + 1) < len(res):
                    res = s[l:i + 1]
        return res