class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # Map closing brackets to their opening brackets
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        # Check each character in the string
        for char in s:

            # If it's an opening bracket, push it onto the stack
            if char in "([{":
                stack.append(char)

            else:
                # If stack is empty, no matching opening bracket exists
                if not stack:
                    return False

                # Remove the last opening bracket
                top = stack.pop()

                # Check if the brackets match
                if pairs[char] != top:
                    return False

        # Valid only if all opening brackets are matched
        return len(stack) == 0
