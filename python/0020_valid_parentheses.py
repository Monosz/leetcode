class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                peek = stack[-1]
                
                if peek == '(' and c == ')':
                    ...
                elif peek == '{' and c == '}':
                    ...
                elif peek == '[' and c == ']':
                    ...
                else:
                    return False
                stack.pop()
        return True if len(stack) == 0 else False
        