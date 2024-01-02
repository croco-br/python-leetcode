from functools import reduce
from typing import List


#works, but is O(n^2)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(len(nums)):
            lst = nums[:i] + nums[i+1:]
            answer.append(self.product_of_list(lst))
                
        return answer
    
    def product_of_list(self, lst):
        return reduce(lambda x, y: x * y, lst, 1)

'''
O(n) from chatgpt
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize prefix and suffix arrays
        prefix_product = [1] * n
        suffix_product = [1] * n
        
        # Calculate prefix products
        prefix = 1
        for i in range(n):
            prefix_product[i] = prefix
            prefix *= nums[i]
        
        # Calculate suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            suffix_product[i] = suffix
            suffix *= nums[i]
        
        # Calculate the final result
        result = [prefix_product[i] * suffix_product[i] for i in range(n)]
        
        return result

'''