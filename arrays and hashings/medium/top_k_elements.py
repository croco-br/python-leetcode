from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for n in nums:
            if n not in hash:
              hash[n] = 1
            else:
              hash[n] += 1
        
        sorted_hash = sorted(hash.items(), key=lambda x: x[1], reverse=True)
        top_k_elements = [item[0] for item in sorted_hash[:k]]

        return top_k_elements