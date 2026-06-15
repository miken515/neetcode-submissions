class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        l, r = 0, 0
        res = 0
        maxFreq = 0

        while l <= r < len(s):
            char = s[r]

            if char not in map:
                map[char] = 1
            else:
                map[char] += 1

            maxFreq = max(maxFreq, map[char])

            while r - l + 1 - maxFreq > k:
                map[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        return res