from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = []

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    if i not in results and j not in results:
                        results.append(i)
                        results.append(j)

        return results
