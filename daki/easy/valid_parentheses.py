class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "(" or ")":
                stack.append(char)
            else:
                return False
