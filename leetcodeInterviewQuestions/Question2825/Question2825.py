class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        idx_str2, length = 0, len(str2)  
        for i in str1:
            if idx_str2 < length and ( ord(str2[idx_str2]) - ord(i) ) % 26 <= 1:
                idx_str2 += 1  
        return idx_str2 == length