from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows and columns
        for i in range(9):
            if not (self.is_valid(board[i]) and self.is_valid([board[j][i] for j in range(9)])):
                return False

        # Check 3x3 boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_valid(box):
                    return False

        return True

    def is_valid(self, lst):
        seen_digits = set()

        for num in lst:
            if num == ".":
                continue
            if num in seen_digits:
                return False
            seen_digits.add(num)

        return True
