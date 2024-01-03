class Solution:
    def isPalindrome(self, x: int) -> bool:
       original = str(x)
       reversed_string = original[::-1]
       
       if(reversed_string == original):
           return True
       
       return False