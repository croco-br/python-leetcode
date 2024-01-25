from typing import List


#works, but not for large lists
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2:
            return nums

        global_max = []
        for i in range(len(nums)):
            current_window = []
            end_window = min(i + k, len(nums))
            for j in range(i, end_window):
                current_window.append(nums[j])
                
            if len(current_window) >= k:
                global_max.append(max(current_window))

        return global_max


# result = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
result = Solution().maxSlidingWindow([1,-1], 1)
print(result)
