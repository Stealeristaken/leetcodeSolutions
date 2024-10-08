class Solution:
    def minSwaps(self, s: str) -> int:
        unmatched_close_bracket_count = 0
        open_bracket = 0
        for i in s:
            if i == '[':
                open_bracket += 1 
            else:
                if open_bracket > 0:
                    open_bracket -= 1 
                else:
                    unmatched_close_bracket_count += 1 
        
        return (unmatched_close_bracket_count+1)//2