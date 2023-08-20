#Question 3 - Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize the result and the sliding window
        result = 0
        window = set()

        # Initialize the left and right pointers of the sliding window
        left = 0
        right = 0

        # Iterate until the right pointer reaches the end of the string
        while right < len(s):
            # Check if the character at the right pointer is not in the window
            if s[right] not in window:
                # If it is not, add it to the window and move the right pointer
                window.add(s[right])
                right += 1
                # Update the result if necessary
                result = max(result, right - left)
            else:
                # If it is, remove the character at the left pointer from the window and move the left pointer
                window.remove(s[left])
                left += 1

        # Return the result
        return result