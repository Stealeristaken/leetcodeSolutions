class Solution:
      def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:
                left += 1
            while right >= left & s[right] == char: #and 
                right -= 1
        return right - left + 1
  
  
  
  
###########################

class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            char = s[l]
            l += 1
            r -= 1
            while l <= r and s[l] == char:
                l += 1
            while l <= r and s[r] == char:
                r -= 1
        
        return r - l + 1