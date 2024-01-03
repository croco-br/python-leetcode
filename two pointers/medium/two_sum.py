from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        results = []
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if numbers[left] + numbers[right] == target:
                results.append(left + 1)
                results.append(right + 1)
                break
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return results
