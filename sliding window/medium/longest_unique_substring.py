class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        chars = {}
        max_length = 0
        start = 0  # Starting index of the current substring

        for i in range(len(s)):
            if s[i] in chars and chars[s[i]] >= start:
                # If the character is repeated within the current substring
                start = chars[s[i]] + 1

            chars[s[i]] = i  # Update the position of the current character
            current_length = i - start + 1
            max_length = max(max_length, current_length)

        return max_length


result = Solution().lengthOfLongestSubstring("anviaj")
print(result)
