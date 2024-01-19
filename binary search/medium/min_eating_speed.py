from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Define the search space
        low, high = 1, max(piles)

        # Perform binary search
        while low < high:
            mid = (low + high) // 2
            hours_required = sum((pile + mid - 1) // mid for pile in piles)

            if hours_required > h:
                # If it takes more hours than allowed, search in the right half
                low = mid + 1
            else:
                # If it takes fewer hours or exactly h, search in the left half
                high = mid

        # The final result is the minimum eating speed
        return low
