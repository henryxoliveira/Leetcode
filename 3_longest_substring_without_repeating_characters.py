class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use a dictionary to store the last index of each character
        char_map = {}
        max_length = 0
        start = 0  # Start of the sliding window
        
        for end in range(len(s)):
            # If the character is already in the current window, move the start pointer
            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1
            
            # Update the last index of the current character
            char_map[s[end]] = end
            
            # Update the maximum length
            max_length = max(max_length, end - start + 1)
        
        return max_length


