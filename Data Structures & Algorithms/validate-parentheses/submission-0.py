class Solution:
    def isValid(self, s: str) -> bool:
        all_brackets_types = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []

        if len(s) % 2 == 1:
            return False

        for char in s:
            if char in all_brackets_types:
                stack.append(char)
            else:
                if stack:
                    top_value = stack[-1] 
                else:
                    return False

                if all_brackets_types[top_value] != char:
                    return False
                else:
                    stack.pop()

        return not stack
