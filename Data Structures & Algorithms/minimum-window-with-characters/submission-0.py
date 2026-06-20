class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = 0
        count = Counter(t)
        window = Counter()
        print(count)
        print(window)

        for i in range(len(s)):
            window[s[i]] += 1
            if window >= count:
                while window[s[l]] > count[s[l]]:
                    window[s[l]] -= 1
                    l += 1
                
                if not res or (i - l + 1) < len(res):
                    res = s[l:i + 1]
        return res