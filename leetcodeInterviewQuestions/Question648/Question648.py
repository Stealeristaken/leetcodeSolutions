from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_words = set(dictionary)
        words = sentence.split()
    
        def find_root(word):
            for j in range(1, len(word)+1):
                if word[:j] in root_words:
                    return word[:j]
            return word
        
        rooted_words = [find_root(word) for word in words]

        return " ".join(rooted_words)