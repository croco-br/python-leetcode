from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements

            left, right = i + 1, len(nums) - 1  # Pointers for the remaining elements

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicate elements
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicate elements

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


results = Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4])
print(results)
