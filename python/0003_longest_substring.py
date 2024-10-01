class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sub: str = ''
        n: int = 0
        for i in range(len(s)):
            if s[i] not in sub:
                sub += s[i]
            else:
                sub = sub[sub.find(s[i])+1:] + s[i]
            n = max(n, len(sub))
            
        return n
        