class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel: str = 'aieuo'

        rev: str = ''
        for c in s[::-1]:
            if c.casefold() in vowel:
                rev += c
        
        ans: str = ''
        j: int = 0
        for i in range(len(s)):
            if s[i].casefold() in vowel:
                ans += rev[j]
                j += 1
            else:
                ans += s[i]

        return ans
        