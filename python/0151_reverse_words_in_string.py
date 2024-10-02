class Solution:
    def reverseWords(self, s: str) -> str:
        words: List[str] = s.split(' ')[::-1]

        words = [w for w in words if w]

        return ' '.join(words).strip()
