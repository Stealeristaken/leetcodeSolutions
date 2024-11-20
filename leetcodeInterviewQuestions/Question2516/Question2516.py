class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        s_count = [0,0,0]
        for c in s:
            s_count[ord(c)- ord('a')] += 1

        if k == 0:
            return 0
        if min(s_count) < k or len(s_count) < 3:
            return -1

        min_mins = float('inf')

        left = 0
        for right in range(len(s)):
            s_count[ord(s[right]) - ord('a')] -= 1

            while min(s_count) < k:
                s_count[ord(s[left]) - ord('a')] += 1
                left += 1
            
            min_mins = min(min_mins, sum(s_count))
        return min_mins
             