class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_count = sum(1 for ch in s if ch == "a")
        b_count = 0  
        min_deletions = n  
        
        for ch in s:
            if ch == "a":
                a_count -= 1  
            min_deletions = min(min_deletions, a_count + b_count)
            if ch == "b":
                b_count += 1  
            
        return min_deletions  
  
  
  
  ############
  
  
class Solution:
    def minimumDeletions(self, s):
        ans, count = 0, 0
        for i in s:
            if i == 'b':
                count += 1
            elif count:
                ans += 1
                count -= 1
        return ans