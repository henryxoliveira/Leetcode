class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        
        # Mapping of closing brackets to their corresponding opening brackets
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            # If it's a closing bracket
            if char in mapping:
                # Check if stack is empty or top doesn't match
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)
        
        # String is valid if stack is empty (all brackets matched)
        return len(stack) == 0

