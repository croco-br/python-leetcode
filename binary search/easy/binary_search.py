from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if len(nums) == 0:
            return -1

        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


print(Solution().search([-1,0,3,5,9,12], 9))
