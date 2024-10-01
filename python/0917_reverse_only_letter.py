class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        rev: str = s[::-1]
        res: str = ''

        j: int = 0
        for i in range(len(s)):
            if s[i].isalpha():
                while not rev[j].isalpha():
                    j += 1
                res += rev[j]
                j += 1
            else:
                res += s[i]

        return res
            