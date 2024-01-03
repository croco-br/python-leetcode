class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    
        filtered_string = ''.join(char.lower() for char in s if char.lower() in allowed_chars)
        
        return filtered_string == filtered_string[::-1]
