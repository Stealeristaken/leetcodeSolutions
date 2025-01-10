from typing import List
from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required=Counter()
        for word in words2:
            required |= Counter(word)
        return [word for word in words1 if not required-Counter(word)]    
