class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            elif char in [")", "}", "]"]:
                if len(stack) == 0 or bracket_mapping[char] != stack.pop():
                    return False

        return len(stack) == 0
