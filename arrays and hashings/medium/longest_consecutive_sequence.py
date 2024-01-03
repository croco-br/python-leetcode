from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique = set(nums)
        longest_streak = 0

        for num in unique:
            if num - 1 not in unique:  # Start of a potential streak
                current_num = num
                current_streak = 1

                while current_num + 1 in unique:  # Extend the streak
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
