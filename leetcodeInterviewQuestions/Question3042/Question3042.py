from typing import List 

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    count+=1
        return count
    
    def isPrefixAndSuffix(self, word, secondWord):
        if secondWord.startswith(word) and secondWord.endswith(word):
            return True
        return False