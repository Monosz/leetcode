class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string: str = ''

        i = j = 0
        while True:
            if i < len(word1):
                string += word1[i]
                i += 1
            if j < len(word2):
                string += word2[j]
                j += 1
            if i == len(word1) and j == len(word2):
                break

        return string
        