class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s): return False
        odd_cnt = 0
        
        for key, val in Counter(s).items():
            if val % 2 == 1:
                odd_cnt += 1

        return True if odd_cnt <= k else False