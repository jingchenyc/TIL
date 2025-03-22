class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        for c in s:
            if c in '({[':
                left.append(c)
            else:
                if left and self.leftOf(c) == left[-1]:
                    left.pop()
                else:
                    return False
        return not left

    def leftOf(self, c:str) -> str:
        if c == ')':
            return '('
        if c == ']':
            return '['
        return '{'
