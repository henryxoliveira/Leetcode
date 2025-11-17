from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Check if s2 contains a permutation of s1 using sliding window approach.
        
        Time Complexity: O(n) where n is the length of s2
        Space Complexity: O(1) since we use fixed-size arrays for character counts
        """
        n1, n2 = len(s1), len(s2)
        
        # If s1 is longer than s2, no permutation can exist
        if n1 > n2:
            return False
        
        # Count characters in s1
        s1_count = Counter(s1)
        
        # Initialize sliding window with first n1 characters of s2
        window_count = Counter(s2[:n1])
        
        # Check if the first window matches
        if window_count == s1_count:
            return True
        
        # Slide the window through s2
        for i in range(n1, n2):
            # Remove leftmost character from window
            left_char = s2[i - n1]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            # Add new character to window
            right_char = s2[i]
            window_count[right_char] += 1
            
            # Check if current window matches s1
            if window_count == s1_count:
                return True
        
        return False

