class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        letters = {}

        for let in s:
            letters[let] = letters.get(let, 0) + 1
        
        for let in t:
            if let in letters:
                letters[let] -= 1
                if letters[let] < 0:
                    return False
            else:
                return False
        
        return all(l == 0 for l in letters.values())
