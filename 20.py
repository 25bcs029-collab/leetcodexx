class Solution:
    def isValid(self, s):
        stack = []
        matching = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in '({[':
                stack.append(char)  # push opening bracket
            else:
                # closing bracket — check if stack is empty or top doesn't match
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0  # valid only if nothing is left unmatched
