from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        result = []

        stack = ["("]
        while stack:
            current = stack.pop()
            open_count = current.count("(")
            close_count = current.count(")")

            if open_count < n:
                stack.append(current + "(")

            if close_count < open_count:
                stack.append(current + ")")

            if len(current) == 2 * n:
                result.append(current)

        return result
