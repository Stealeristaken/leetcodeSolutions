class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for char in s:
            if char == '(': low, high = low + 1, high + 1
            elif char == ')': low, high = low - 1, high - 1
            else: low, high = low - 1, high + 1
            if high < 0: return False
            low = max(low, 0)
        return low == 0
  
  
########## Another Solution ##########    

class Solution:
    def checkValidString(self, s: str) -> bool:
        l_min, l_max = 0, 0

        for c in s:
            if c == '(':
                l_min += 1
                l_max += 1
            elif c == ')':
                if l_max <= 0:
                    return False

                l_min = max(0, l_min - 1)
                l_max -= 1
            else:
                l_min = max(0, l_min - 1)
                l_max += 1
        
        return l_min == 0